api_key = "8f19c2c2e8a325a07b2c35bfe43d861b"

import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
from PIL import Image, ImageTk

# Huge thanks to 

def get_weather(city):
    api_key_one = "8f19c2c2e8a325a07b2c35bfe43d861b"
    # api_key_two = "ce6207a53a45475db3c90051252703"
    url_one = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key_one}'
    # url_two = f'http://api.weatherapi.com/v1/forecast.json?key={api_key_two}&q={city}&days=1&aqi=no&alerts=no'
    res_one = requests.get(url_one)
    # res_two = requests.get(url_two)

    # If the user enters error, the program will output 'City Not Found'
    if res_one.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    # if res_two.status_code == 404:
        # messagebox.showerror("Error", "City Not Found")
        # return None
    
    weather_one = res_one.json()
    # weather_two = res_two.json()
    print(f'{weather_one}\n')
    # print(weather_two)
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

# Create a window in ttkbootstrap
root = ttkbootstrap.Window(themename="morph")
# Give the window a name
root.title("Weather App From Youtube")
# Set the default resolution of the window
root.geometry("600x600")

# Display the Name of the weather application
title_text = tk.Label(root, text="WWeather", font="Helvetica, 36")
title_text.pack(pady=15)

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

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()