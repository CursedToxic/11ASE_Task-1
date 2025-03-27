api_key = "8f19c2c2e8a325a07b2c35bfe43d861b"

import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
from PIL import Image, ImageTk

# Text1 = Label(root, text= "This is to see if you are an idiot")
# Text2 = Label(root, text= "If you are reading this you have spent at least 1 second on this app")
# Text1.grid(row=0, column=0)
# Text2.grid(row=0, column=100)
# Text1.pack()
# Text2.pack()

# def gullibility():
      # print(f"This user has clicked the button: Gullible")

# def darkMode():
    # darkText = Label(root, text= "Dark Mode not activated", fg="white")
    # is_dark = root.cget("bg")
    # is_light = ttkbootstrap.Window(themename="morph") if is_dark == ttkbootstrap(themename="superhero") else ttkbootstrap(themename="superhero")
    # is_light = "white" if is_dark == "black" else "black"
    # darkText = root.configure(background= is_light)
    # darkText.pack()

# Button1 = tk.Button(root, text= "Click to see if you are dumb")
# Button2 = tk.Button(root, text= "Click to see if you are gullible", command=gullibility)
# Button3 = tk.Button(root, text= "Dark Mode", bg= "black", fg="white", command=darkMode)
# Button1.grid(row=0, column=10)
# Button2.grid(row=10, column=0)
# Button3.grid(row= 1, column=1)
# Button1.pack()
# Button2.pack()
# Button3.pack()

def get_weather(city):
    api_key_one = "8f19c2c2e8a325a07b2c35bfe43d861b"
    # api_key_two = "ce6207a53a45475db3c90051252703"
    url_one = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key_one}'
    # url_two = f'http://api.weatherapi.com/v1/forecast.json?key={api_key_two}&q={city}&days=1&aqi=no&alerts=no'
    res_one = requests.get(url_one)
    # res_two = requests.get(url_two)

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

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App From Youtube")
root.geometry("600x600")

title_text = tk.Label(root, text="W-Weather", font="Helvetica, 36")
title_text.pack(pady=15)

city_entry = ttkbootstrap.Entry(root, font= "Helvetica, 18")
city_entry.pack(pady=10)
root.bind('<Return>', get_weather)

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