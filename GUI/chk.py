# Python program to change menu background
# color of Tkinter's Option Menu

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Give title to your GUI app
app.title("Vinayak App")

# Construct the label in your app
l1 = Label(app, text="Choose the week day here")

# Display the label l1
l1.grid()

# Construct the Options Menu widget in your app
text1 = StringVar()

# Set the value you wish to see by default
text1.set("Choose here")

# Create options from the Option Menu
w = OptionMenu(app, text1, "Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday")

# Se the background color of Options Menu to green
w.config(bg="GREEN", fg="WHITE")

# Set the background color of Displayed Options to Red
w["menu"].config(bg="RED")

# Display the Options Menu
w.grid(pady=20)

# Make the loop for displaying app
app.mainloop()
