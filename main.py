api_key = "8f19c2c2e8a325a07b2c35bfe43d861b"

import requests
from tkinter import *
import tkinter as tk

### Thanks to Arpan Neupane for the text based application, I have followed his video tutorial.
user_input = input("Enter City: ")

weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}')

if weather_data.json()['cod'] == '404':
       print("No City Found")

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    print(f"The weather in {user_input} is {weather}.")
    print(f"The temperature in {user_input} is {temp}°C.")

### From here on the rest is by me

root = tk.Tk()
root.title("Window")
root.configure(background = "white")
# root.minsize(200, 200)
# root.geometry("1280x720+400+200")

Text1 = Label(root, text= "This is to see if you are an idiot")
Text2 = Label(root, text= "If you are reading this you have spent at least 1 second on this app")
# Text1.grid(row=0, column=0)
# Text2.grid(row=0, column=100)
Text1.pack()
Text2.pack()

def gullibility():
      print(f"This user has clicked the button: Gullible")

def darkMode():
    # darkText = Label(root, text= "Dark Mode not activated", fg="white")
        is_dark = root.cget("bg")
        is_light = "white" if is_dark == "black" else "black"
        darkText = root.configure(background= is_light)
    # darkText.pack()

Button1 = tk.Button(root, text= "Click to see if you are dumb")
Button2 = tk.Button(root, text= "Click to see if you are gullible", command=gullibility)
Button3 = tk.Button(root, text= "Dark Mode", bg= "black", fg="white", command=darkMode)
# Button1.grid(row=0, column=10)
# Button2.grid(row=10, column=0)
# Button3.grid(row= 1, column=1)

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()