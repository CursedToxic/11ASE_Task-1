# 11ASE Task 1 2025 - WWeather App

#### By Victor Guo

## Requirements Definition
### Functional Requirements
**Data Retrieval:**\
 What does the user need to be able to view in the system?\
 The user needs to be able to choose what data to delete, however, this data must not be from the API itself. This ensures that the application does not break due to the user unknowingly deleting something within the API that might stop the program from functioning properly.

**User Interface:**\
 What is required for the user to interact with the system?\
 The ability to click on buttons and read text is needed to use the program. It should be extremely easy to navigate through the user interface and if the user cannot understand, there should be a navigation guide on top of the search bar.

**Data Display:**\
 The User must be able to read the data from the API but not be able to change without permission. This again helps keep the application running. The data must also be as accurate as possible in order to make sure that the user recieves the right information upon using the app.

### Non-Functional Requirements
**Performance:**\
 This program needs to run smoothly on even the oldest devices (the test will be my MacBook Air from 2013, an 11 year old machine which struggles to run the web browser). Performance should be maintained when using different platforms, so the user can user is confident that they can run it on their computer.

**Reliability:**\
 The system actually does need to be extremely reliable as the user's data is a top priority and must not be leaked, so the system needs to be extremely reliable and store the data securely on all operating systems, and must not be flagged as insecure on any of them. This way the user who is going to install the application can be sure that they are not harming their computer.

**Usability and Accessibility:**\
  The system needs to be easy to navigate so that people who are not very familiar with computers can easily understand how it works. All there will need to be is a how to file showing what each button leads to. This program will also need to work on all desktop operating systems (will test using Windows, MacOS and Some Linux Kernels), which will make it widely accessible and run with no compatibility issues.

## Determining Specifications
### Functional Specifications
**User Requirements:**\
What does the user need to be able to do? List all specifications here.\
The user needs to be able to easily navigate the application even if they have never encountered it before, hopefully even without the guide. 

**Inputs & Outputs:**\
What inputs will the system need to accept and what outputs will it need to display?\
inputs: text containing the city
outputs: weather for that city, this includes the temperature in degrees celsius and the weather description e.g. partly cloudy.
inputs: buttons
outputs: fetch and output data from the API.

**Core Features:**\
The program needs to accept user input so that they can enter the name of a valid city. Another aspect of function is the ability to detect invalid places so that the weather data that is displayed is as accurate as possible so that the user experience will not be negatively affected.The user needs to also be able to search for the place with a button once they have entered the name of the desired place into the search box (this would be preffered if the user could also press ENTER for the same function).

**User Interaction:**\
How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?\
The program needs to be able to display the temperature and the description of the weather from the API in a GUI (Graphical User Interface). This makes it easy for the user to find exactly what they want without needing to know much about using a computer.

**Error Handling:**\
What possible errors could you face that need to be handled by the system?\
An error that could be faced that needs to be handled by the system is in the instance that the user enters an invalid location. This will be handled by a pop-up message that reads 'City Not Found'. 

### Non-Functional Specifications
**Performance:**\
The system should fetch weather data as fast as possible so that the user does not feel as though they are working with a bloated application. The application should also feel smooth while running, having smooth animations and seamless theme changes, ensuring that it performs well.

**Useability / Accessibility:**\
How might you make your application more accessible? What could you do with the User Interface to improve usability?\
The user interface must be at least semi-aesthetic in order to make the user feel at home, preventing strain due to unnecessary text. On top of this, the application should launch the first time after installing the dependencies so that the user needs minimal time to retrieve weather data.

**Reliability:**\
A potential issue that needs to be adressed is the incorrect data when fetching data from the API. An example of this is when the user searches up a city such as 'Zhuzhou' (real place) and it comes up as 'Jianning' instead. This cannot be fixed as there seems to be a mismatch of data from the API itself (it labels Zhuzhou as Jianning and Jianning as something else.) Another issue is that the current weather app cannot distinguish places with the same name. These can hopefully be fixed easily.

## Design
### Gantt Chart
![alt text](images/Gantt%20Chart.png)
Link to Gantt Chart: https://lucid.app/lucidspark/162a4a9b-0462-4f05-9b21-b1997af60854/edit?invitationId=inv_9c51b1d8-6a9c-4b3f-bf6d-b49fa2d28f11&page=uDe-dIt-NWfS#

### Flowchart
![alt text](images/main.png)
![alt text](images/getWeather.png)
![alt text](images/search.png)

### Structure Chart

### Data Dictionary
|Variable|Data Type|Format for Display|Size in Bytes|Size for Display|Description|Example|Validation|
|--------|---------|------------------|-------------|----------------|-----------|-------|----------|
|location|string|text|50|50|the name of the place|Sydney|Must be place on google maps|
|temperature|float|2 decimal number|8|4|the temparature at the place|21.62|must be between -273.15 and 100.00|
|degrees|string|2 character measurement|20|20|measurement for temperature|°C|must be either °C|
|description|string|text|100|100|the weather for that place|Partly Cloudy|must be valid desription|

### Pseudocode
``` python
BEGIN mainloop
  WHILE running
    FUNCTION get_weather
    FUNCTION search
    FUNCTION change_theme
  ENDWHILE
END mainloop

BEGIN get_weather
  IF city status code IS 404 THEN
    DISPLAY City Not Found
  ELSE
    RETURN icon_url
    RETURN temperature
    RETURN description
    RETURN city
    RETURN country
  ENDIF
END get_weather

BEGIN change_theme
  IF selected_theme is selected THEN
    use selected_theme
  ENDIF

BEGIN search
  INPUT city
  result = FUNCTION get_weather
  IF result IS NONE THEN
        RETURN NONE
  ELSE
    FUNCTION get_weather
  ENDIF
```
## Development

## Integration
Documented Commit No.1:
```python
# my_module.py 

import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
from PIL import Image, ImageTk

# Huge thanks to some guy on yt for the tutorial.

api_key_one = "8f19c2c2e8a325a07b2c35bfe43d861b"
    # api_key_two = "ce6207a53a45475db3c90051252703"
url_one = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key_one}'
    # url_two = f'http://api.weatherapi.com/v1/forecast.json?key={api_key_two}&q={city}&days=1&aqi=no&alerts=no'
res_one = requests.get(url_one)
    # res_two = requests.get(url_two)

def get_weather(city):
    # If the user enters error, the program will output 'City Not Found'
    if res_one.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    # if res_two.status_code == 404:
        # messagebox.showerror("Error", "City Not Found")
        # return None
    
    weather_one = res_one.json()
    # weather_two = res_two.json()
    icon_id = weather_one["weather"][0]["icon"]
    temperature = weather_one["main"]["temp"]
    description = weather_one["weather"][0]["description"]
    city = weather_one["name"]
    country = weather_one["sys"]["country"]

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

# Function to change the theme
def change_theme(event):
    selected_theme = theme_menu.get()
    root.style.theme_use(selected_theme)

# Create a window in ttkbootstrap
root = ttkbootstrap.Window(themename="morph")
# Give the window a name
root.title("WWeather")
# Sets the resolution that the window will open at
root.geometry("1024x768")
# Set the minimum resolution or 'size' of the window
root.minsize(width=800, height=500)

def resize_text(event):
    # Calculate font size based on window width
    new_font_size = int(event.width/20)
    if new_font_size < 36:  # Set a minimum font size
        new_font_size = 36
    title_text.config(font=("Helvetica", new_font_size))


# Display the Name of the weather application
title_text = tk.Label(root, text="WWeather", font=("Helvetica", 36))
title_text.pack(expand=True, fill=tk.BOTH, pady=5)

# Bind the <Configure> event to adjust text size dynamically
root.bind("<Configure>", resize_text)

# Give the user a space to enter their city of choice
city_entry = ttkbootstrap.Entry(root, font= "Helvetica, 18")
city_entry.pack(pady=10)

# Make the user able to simply press the ENTER key to fetch weather data (does not work yet)
root.bind('<Return>', get_weather)


# Create and display a search button in order to fetch the weather
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)


location_label = tk.Label(root, font = "Helvetica, 25")
location_label.pack(pady=20)

# Create the icon for the weather description and place it in the GUI
icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

theme_menu = ttkbootstrap.Combobox(root, values=root.style.theme_names(), state="readonly")
theme_menu.set("Select Theme")  # Default text
theme_menu.pack(pady=5)
theme_menu.bind("<<ComboboxSelected>>", change_theme)  # Event binding

root.mainloop()

# main.py
m.root.mainloop()
```
Documented Commit No.2
```python
import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
from PIL import Image, ImageTk

# Huge thanks to 

def get_weather(city):
    api_key_one = "8f19c2c2e8a325a07b2c35bfe43d861b"
    url_one = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key_one}'
    res_one = requests.get(url_one)
    
    # If the user enters error, the program will output 'City Not Found'
    if res_one.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    ### Below is for the other, more accurate WeatherAPI
    # api_key_two = "ce6207a53a45475db3c90051252703"
    # url_two = f'http://api.weatherapi.com/v1/forecast.json?key={api_key_two}&q={city}&days=1&aqi=no&alerts=no'
    # res_two = requests.get(url_two)
    # if res_two.status_code == 404:
        # messagebox.showerror("Error", "City Not Found")
        # return None
    
    weather_one = res_one.json()
    # weather_two = res_two.json()
    icon_id = weather_one["weather"][0]["icon"]
    temperature = weather_one["main"]["temp"]
    description = weather_one["weather"][0]["description"]
    city = weather_one["name"]
    country = weather_one["sys"]["country"]

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

# Function to change the theme
def change_theme(event):
    selected_theme = theme_menu.get()
    root.style.theme_use(selected_theme)

# Create a window in ttkbootstrap
root = ttkbootstrap.Window(themename="morph")
# Give the window a name
root.title("WWeather")
# Sets the resolution that the window will open at
root.geometry("1024x768")
# Set the minimum resolution or 'size' of the window
root.minsize(width=800, height=500)

def resize_text(event):
    # Calculate font size based on window width
    new_font_size = int(event.width/20)
    if new_font_size < 36:  # Set a minimum font size
        new_font_size = 36
    title_text.config(font=("Helvetica", new_font_size))

# Display the Name of the weather application
title_text = tk.Label(root, text="WWeather", font=("Helvetica", 36))
title_text.pack(expand=True, fill=tk.BOTH, pady=5)

# Bind the <Configure> event to adjust text size dynamically
root.bind("<Configure>", resize_text)

# Give the user a space to enter their city of choice
city_entry = ttkbootstrap.Entry(root, font= "Helvetica, 18")
city_entry.pack(pady=10)

# Make the user able to simply press the ENTER key to fetch weather data (does not work yet)
root.bind('<Return>', get_weather)

# Create and display a search button in order to fetch the weather
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Outputs the location entered by the user
location_label = tk.Label(root, font= "Helvetica, 25")
location_label.pack(pady=20)

# Create the icon for the weather description and place it in the GUI
icon_label = tk.Label(root)
icon_label.pack()

# This will output the temperature of the entered location
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# This will be the output of the description of the weather
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

#This uses the style.themenames function in Combobox in ttkbootstrap
theme_menu = ttkbootstrap.Combobox(root, values=root.style.theme_names(), state="readonly") # make it so that the user cannot add any themes that do not exist
theme_menu.set("Select Theme")  # Default text
theme_menu.pack(pady=5)
theme_menu.bind("<<ComboboxSelected>>", change_theme)  # Bind the selection of the theme menu to a function that changes the theme

root.mainloop()
```
## Testing and Debugging

## Installation

## Maintenance