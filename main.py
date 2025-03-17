from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Window")
root.configure(background = "white")
root.minsize(200, 200)
root.geometry("1280x720+400+200")

Text1 = Label(root, text= "This is to see if you are an idiot")
Text2 = Label(root, text= "If you are reading this you have spent at least 1 second on this app")
# Text1.grid(row=0, column=0)
# Text2.grid(row=0, column=100)
Text1.pack()
Text2.pack()

def gullibility():
      times = Button2.clicked()
      print(f"This user has clicked the button {times} times")

def darkMode():
    # darkText = Label(root, text= "Dark Mode not activated", fg="white")
        is_dark = root.cget("bg")
        is_light = "white" if is_dark == "black" else "black"
        darkText = root.configure(background= is_light)
    # darkText.pack()
        while root.configure(background= is_dark):
                Button3 = tk.Button(root, text= "Light Mode", bg= "white", fg="black", command=darkMode)
                if root.configure(background= is_light):
                    pass 
                else:
                    continue

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