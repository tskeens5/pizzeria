import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def validate_entry(entry, datatype):
    """
    Validates the input from the entry widget to ensure it matches the expected data type.
    """
    value = entry.get().strip()
    if not value:
        messagebox.showerror("Input Error", "Entry cannot be empty")
        return False
    if datatype == "int":
        try:
            int(value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter an integer value")
            return False
    return True

def show_pizza_window():
    """
    Opens the pizza selection window.
    """
    pizza_window = tk.Toplevel(app)
    pizza_window.title("Pizza Choices")
    
    label = tk.Label(pizza_window, text="Select Your Pizza")
    label.pack()

    pizza_options = ["Pepperoni", "Margarita", "BBQ Chicken", "Vegetarian"]
    pizza_var = tk.StringVar(value=pizza_options[0])

    for option in pizza_options:
        radio = tk.Radiobutton(pizza_window, text=option, variable=pizza_var, value=option)
        radio.pack()

    def submit_pizza():
        selection = pizza_var.get()
        messagebox.showinfo("Selection", f"You selected: {selection}")

    submit_button = tk.Button(pizza_window, text="Submit", command=submit_pizza)
    submit_button.pack()

def show_sides_window():
    """
    Opens the sides selection window.
    """
    sides_window = tk.Toplevel(app)
    sides_window.title("Side Choices")

    label = tk.Label(sides_window, text="Select Your Sides")
    label.pack()

    sides_options = ["Garlic Bread", "Chicken Wings", "Mozzarella Sticks", "Salad"]
    sides_var = tk.StringVar(value=sides_options[0])

    for option in sides_options:
        radio = tk.Radiobutton(sides_window, text=option, variable=sides_var, value=option)
        radio.pack()

    def submit_sides():
        selection = sides_var.get()
        messagebox.showinfo("Selection", f"You selected: {selection}")

    submit_button = tk.Button(sides_window, text="Submit", command=submit_sides)
    submit_button.pack()

def show_drinks_window():
    """
    Opens the drinks selection window.
    """
    drinks_window = tk.Toplevel(app)
    drinks_window.title("Drink Choices")

    label = tk.Label(drinks_window, text="Select Your Drink")
    label.pack()

    drinks_options = ["Coke", "Sprite", "Water", "Juice"]
    drinks_var = tk.StringVar(value=drinks_options[0])

    for option in drinks_options:
        radio = tk.Radiobutton(drinks_window, text=option, variable=drinks_var, value=option)
        radio.pack()

    def submit_drinks():
        selection = drinks_var.get()
        messagebox.showinfo("Selection", f"You selected: {selection}")

    submit_button = tk.Button(drinks_window, text="Submit", command=submit_drinks)
    submit_button.pack()

def exit_application():
    """
    Exits the application.
    """
    app.quit()

app = tk.Tk()
app.title("Tom's Pizzeria")

# Load images
try:
    pizza_image = Image.open("pizza.jpg")
    pizza_photo = ImageTk.PhotoImage(pizza_image)
except Exception as e:
    pizza_photo = None
    messagebox.showerror("Image Error", f"Failed to load pizza image: {e}")

try:
    sides_image = Image.open("sides.jpg")
    sides_photo = ImageTk.PhotoImage(sides_image)
except Exception as e:
    sides_photo = None
    messagebox.showerror("Image Error", f"Failed to load sides image: {e}")

# Labels
welcome_label = tk.Label(app, text="Welcome to Tom's Pizzeria!")
welcome_label.pack()

if pizza_photo:
    pizza_label = tk.Label(app, image=pizza_photo, text="Pizza Image", compound="top")
    pizza_label.pack()

if sides_photo:
    sides_label = tk.Label(app, image=sides_photo, text="Sides Image", compound="top")
    sides_label.pack()

# Buttons
pizza_button = tk.Button(app, text="Choose Pizza", command=show_pizza_window)
pizza_button.pack()

sides_button = tk.Button(app, text="Choose Sides", command=show_sides_window)
sides_button.pack()

drinks_button = tk.Button(app, text="Choose Drinks", command=show_drinks_window)
drinks_button.pack()

exit_button = tk.Button(app, text="Exit", command=exit_application)
exit_button.pack()

app.mainloop()