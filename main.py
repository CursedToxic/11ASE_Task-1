from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Window")
root.configure(background = "white")
root.minsize(200, 200)
root.geometry("1280x720+500+250")

Text1 = Label(root, text= "This is to see if you are an idiot")
Text2 = Label(root, text= "If you are reading this you have spent at least 1 second on this app")
# Text1.grid(row=0, column=0)
# Text2.grid(row=0, column=100)
Text1.pack()
Text2.pack()

def darkMode():
    # darkText = Label(root, text= "Dark Mode not activated", fg="white")
        darkText = root.configure(background= "black")
        darkText.pack()

Button1 = tk.Button(root, text= "Click to see if you are dumb")
Button2 = tk.Button(root, text= "Click to see if you are gullible")
Button3 = tk.Button(root, text= "Dark Mode", bg= "black", fg="white", command=darkMode)
# Button1.grid(row=0, column=10)
# Button2.grid(row=10, column=0)
# Button3.grid(row= 1, column=1)

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()