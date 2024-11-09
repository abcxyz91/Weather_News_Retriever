from models import Weather, News
from pathlib import Path
from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    """ Pretty print a welcome text for the user """
    welcome()

    """ Get info from user from the text file, if not exist, asking for user current city """
    city = get_city()
    category = get_category()

    """ Return weather info today """
    weather = Weather(city)
    weather.update()
    weather.display_weather()

    """ Return tops news today """
    news = News(category)
    news.update()
    news.display_news()

    """ Ask user if he wants to check other news or not, if not, say goodbye and close """
    while True:
        confirm = input("\nDo you want to check other news category? Yes/No? ")
        if confirm == "y" or confirm == "yes":
            category = get_category()
            news = News(category)
            news.update()
            news.display_news()
        elif confirm == "n" or confirm == "no":
            goodbye()
            sys.exit()



def get_city():
    """ Ask user to input a city name and remember user's city for the next time """
    path = Path("city.txt")
    if path.exists():
        city = path.read_text(encoding="utf-8")
        while True:
            confirm = input(f"Is your current city is {city.title()}? Yes/No ").strip().lower()
            if confirm == "y" or confirm == "yes":
                return city
            elif confirm == "n" or confirm == "no":
                while True:
                    city = input("Please input your current city: ").strip().lower()
                    if city != "":
                        path.write_text(city)
                        return city
    else:
        while True:
            city = input("Please input your current city: ").strip().lower()
            if city != "":
                path.write_text(city)
                return city


def get_category():
    """ Ask user to choose the news category from the list of category """
    categories = {
        "1": "business",
        "2": "entertainment",
        "3": "health",
        "4": "science",
        "5": "sports",
        "6": "technology"
    }

    while True:
        print("Please choose one of the news categories below:")
        for num, category in categories.items():
            print(f"{num}. {category.title()}")

        choice = input().strip()
        if choice in categories.keys():
            return categories[choice]
        else:
            print("Invalid category")

def welcome():
    welcome_text = "How are you?"
    figlet.setFont(font="standard")
    print(figlet.renderText(welcome_text))
    return True


def goodbye():
    goodbye_text = "Have a good day!"
    figlet.setFont(font="standard")
    print(figlet.renderText(goodbye_text))
    return True


if __name__ == "__main__":
    main()
