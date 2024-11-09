import requests
from tabulate import tabulate


class Weather:
    """ Setup class constant """
    API_KEY = "YOUR API KEY HERE"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


    def __init__(self, city):
        """ Initialize the class, check the input and setup class attributes """
        if not city:
            raise ValueError("Missing city")

        self.city = city
        self.temperature = None
        self.humidity = None
        self.description = None
        self.country = None
        self.status_code = None

    def update(self):
        """ Try getting API response by requests, if status_code 200, assign class attributes to value returned by the API
        If not, show the error message """
        request_url = f"{Weather.BASE_URL}?q={self.city}&appid={Weather.API_KEY}&units=metric"
        try:
            response = requests.get(request_url)
            if response.status_code == 200:
                data = response.json()
                self.temperature = round(data["main"]["temp"])
                self.humidity = data["main"]["humidity"]
                self.description = data["weather"][0]["description"]
                self.country = data["sys"]["country"]
                self.status_code = 200
            else:
                print(f"Error occurred. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request error: {e}")
            self.status_code = None


    def display_weather(self):
        """ If status code 200, pretty print the result by tabulate library, otherwise, show error message """
        if self.status_code == 200:
            weather_data = [{
                "Temperature": f"{self.temperature}°C",
                "Humidity": f"{self.humidity}%",
                "Description": self.description.title()
            }]
            print(f"The weather today in {self.city.title()}")
            print(tabulate(weather_data, headers="keys", tablefmt="grid"))
        else:
            print("Unable to show weather data")


class News:
    """ Setup class constant """
    API_KEY = "YOUR API KEY HERE"
    BASE_URL = "https://newsapi.org/v2/top-headlines?country=us"

    VALID_CATEGORY = ["business", "entertainment", "health", "science", "sports", "technology"]

    def __init__(self, category):
        """ Initialize the class, setup class attributes """
        if not category:
            raise ValueError("Missing category")

        if category not in self.VALID_CATEGORY:
            raise ValueError("Invalid category")

        self.category = category
        self.data = []
        self.status_code = None


    def update(self):
        """ Try getting API response by requests, if status_code 200, assign class attributes to value returned by the API
        If not, show the error message """
        request_url = f"{News.BASE_URL}&category={self.category}&apiKey={News.API_KEY}"
        try:
            response = requests.get(request_url)
            if response.status_code == 200:
                data = response.json()
                self.data = []
                # Print the maximum 10 news using list slicing
                for article in data["articles"][:10]:
                    # Format the hyperlink properly using ANSI escape codes
                    url = article["url"]
                    source_name = article["source"]["name"]
                    hyperlink = f"\x1b]8;;{url}\x1b\\{source_name}\x1b]8;;\x1b\\"

                    # Add each news as a list of dictionary, for tabulate print later
                    self.data.append({
                        "Title": article["title"],
                        "Source": hyperlink
                        })
                self.status_code = 200
            else:
                print(f"Error occurred. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request error: {e}")
            self.status_code = None


    def display_news(self):
        """ If status code 200, pretty print the result by tabulate library, otherwise, show error message """
        if self.status_code == 200:
            print(f"\nThe topten {self.category.title()} news are: ")
            print(tabulate(self.data, headers="keys", tablefmt="grid"))
        else:
            print("Unable to show news data")
