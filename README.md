# Weather and News CLI Application

## Overview
This is a Command Line Interface (CLI) application written in Python that provides users with real-time weather and top news information based on their chosen city and news category. The app is designed for simplicity, user-friendliness, and reusability. It leverages popular APIs to fetch up-to-date data and makes use of basic file storage to remember user preferences. With functionalities neatly organized into two primary classes (`Weather` and `News`) and various utility functions, the application serves as a practical example of structuring a Python application with modular, reusable code.

## Purpose
The primary purpose of this project is to offer users a quick and easy way to retrieve:
1. **Current weather conditions** for a specific city.
2. **Top news headlines** from various categories, such as Business, Health, Sports, etc.

It also aims to help beginners in Python to understand:
- How to make API requests and process JSON data.
- Writing modular and reusable code using classes and functions.
- Working with files for storing simple user data.

## Tools and Libraries Used
The following libraries and tools are used in this project:

- **Python Standard Library**:
  - `Pathlib`: For reading and writing user data to files in a platform-independent way.
  - `sys`: To gracefully exit the application when the user finishes.

- **External Libraries**:
  - **`requests`**: Used to handle HTTP requests for retrieving data from the weather and news APIs.
  - **`tabulate`**: To display information in a clean, tabular format, enhancing readability.
  - **`pyfiglet`**: For generating stylized ASCII art text, used in the welcome and goodbye messages.

> **Note**: The required libraries are listed in `requirements.txt`. You can install them with the following command:
> ```bash
> pip install -r requirements.txt
> ```

## Project Structure
The application has two main components:
1. **`app.py`**: The main application file that handles user interaction, retrieves user inputs, and displays results.
2. **`models.py`**: Contains the core classes (`Weather` and `News`) responsible for managing API requests and formatting the fetched data.

### API Information
The application uses:
- **OpenWeather API** for weather information.
- **News API** for top news headlines.

These APIs require API keys, which are stored in the `Weather` and `News` classes in `helper.py`.

---

## Functions Overview

### `app.py` Functions

1. **`main()`**:
   - The entry point of the application.
   - Displays a welcome message, retrieves user data (city and news category), and initiates data retrieval.
   - Continuously asks if the user wants to fetch other news categories before finally exiting.

2. **`get_city()`**:
   - Checks if a saved city exists (`city.txt` file).
   - If the file exists, it asks the user to confirm if they want to continue with the saved city or enter a new one.
   - If no city is saved, prompts the user to enter their city and saves it for future use.

3. **`get_category()`**:
   - Displays a list of available news categories and prompts the user to choose one.
   - Returns the selected category as a string for further processing in the `News` class.

4. **`welcome()`**:
   - Prints a stylized welcome message using `pyfiglet` for enhanced user experience.

5. **`goodbye()`**:
   - Prints a goodbye message and gracefully ends the application, also using `pyfiglet` for styling.

### `models.py` Classes

1. **`Weather`**:
   - **Purpose**: To manage the retrieval and display of weather data for the specified city.
   - **Attributes**:
     - `city`: The user-specified city for which to fetch weather data.
     - `temperature`, `humidity`, `description`, `country`: Store specific weather details.
   - **Methods**:
     - `update()`: Sends a request to the OpenWeather API, processes the JSON response, and updates weather attributes if the request is successful.
     - `display_weather()`: Displays the weather details in a tabular format using `tabulate`. If data isn’t available (e.g., due to an API error), it shows an error message.

2. **`News`**:
   - **Purpose**: To manage the retrieval and display of top news headlines based on the selected category.
   - **Attributes**:
     - `category`: The news category selected by the user (e.g., business, health).
     - `data`: Holds the list of top news articles retrieved from the News API.
   - **Methods**:
     - `update()`: Sends a request to the News API with the selected category and processes the JSON response.
     - `display_news()`: Shows the top 10 news articles in a tabular format. If data isn’t available, it displays an error message.

---

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Upon starting, the application will:
   - Display a welcome message.
   - Prompt the user to confirm their saved city or enter a new one.
   - Prompt the user to select a news category.
   - Fetch and display the weather data and top news headlines.

3. The user can then choose to:
   - View another news category.
   - Exit the application, which will display a goodbye message.

---

## Summary

This CLI application is a beginner-friendly Python project that demonstrates practical use of APIs, file handling, and user interaction through the command line. By organizing functionalities into classes and utility functions, it achieves modularity and ease of maintenance. The `Weather` and `News` classes encapsulate the data retrieval logic, making it straightforward to extend or modify the application.

The project is suitable for anyone looking to:
- Learn about API integrations in Python.
- Practice organizing Python projects with a focus on modularity.
- Build a useful, real-world application that provides timely information.

This README serves as a guide for installation, usage, and understanding the underlying structure of the application.
