import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Function to change the theme
def change_theme(event):
    selected_theme = theme_menu.get()
    app.style.theme_use(selected_theme)

# Create the main application window
app = ttk.Window(themename="cosmo")
app.title("Theme Changer")
app.geometry("300x150")

# Dropdown menu for selecting themes
theme_menu = ttk.Combobox(app, values=app.style.theme_names(), state="readonly")
theme_menu.set("Select Theme")  # Default text
theme_menu.pack(pady=30)
theme_menu.bind("<<ComboboxSelected>>", change_theme)  # Event binding

# Start the application
app.mainloop()