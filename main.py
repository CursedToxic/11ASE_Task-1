api_key = "8f19c2c2e8a325a07b2c35bfe43d861b"

import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
# from PIL import Image, ImageTk

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App From Youtube")
root.geometry("400x400")

title_text = tk.Label(root, text="W-Weather", font="Helvetica, 36")
title_text.pack(pady=15)

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

city_entry = ttkbootstrap.Entry(root, font= "Helvetica, 18")
city_entry.pack(pady=5)

search_button = ttkbootstrap.Button(root, text="Get Weather", command=search, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font= "Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# Button1 = tk.Button(root, text= "Click to see if you are dumb")
# Button2 = tk.Button(root, text= "Click to see if you are gullible", command=gullibility)
# Button3 = tk.Button(root, text= "Dark Mode", bg= "black", fg="white", command=darkMode)
# Button1.grid(row=0, column=10)
# Button2.grid(row=10, column=0)
# Button3.grid(row= 1, column=1)
# Button1.pack()
# Button2.pack()
# Button3.pack()

root.mainloop()