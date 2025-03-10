import tkinter as tk

root  = tk.Tk()
root.title("Window")
root.configure(background = "white")
root.minsize(200, 200)
root.geometry("600x600+400+200")

Button1 = tk.Button(root, text= "Click to see if you are dumb").pack()
Button2 = tk.Button(root, text= "Click to see if you are gullible").pack()
root.mainloop()