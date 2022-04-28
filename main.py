from tkinter import *
from tkinter import messagebox
import random


# --------------------------Documentation -------------------- #
# Author: Brian Thompson #
# Password Manager that allows user to store their user/email and password in a text file locally in their computer #






# --------------------------saving password -------------------- #

# the save function takes inputs from users website, email, and password to save this info lcoally in a data.txt file #
# to fetch the text in the entry, the get method is used #

def save():

    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()


    # If users password is not at least at characters long they will get this warning box #
    if 1 <= len(password) < 8:
        messagebox.showerror(title="Oops", message=f"Password should be at least 8 characters long")

    # when the user leaves the website, email, or password field empty, they get a warning box #
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message=f"Please don't leave any fields empty!")


    # if the user has inputed values in all the fields, then it will work #
    elif len(password) >=8:
        userSaysYes = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {email}" 
                                                  f"\nPassword: {password} \nDo you want to save?")

# when they click yes their info will write to the data.txt file. to trigger userSaysYes, add an if statement #
# the data.txt is the text file that will store the information from get method #
# "a" is used to append the information so that each entry is stored in the data.txt file#
        if userSaysYes:
            with open("data.txt","a") as data_file:

            # this will write the data from the get method to the file i this format #
                # website | email | password #
                data_file.write(f" Website: {website} | User: {email} | Password: {password}\n")

            # This deletes an entry the user made after they hit the add button, so it can take the next one. the zero is inputed so it can start at the begining #
            websiteEntry.delete(0,END)
            passwordEntry.delete(0,END)





# --------------------------GUI -------------------- #

# Window for the password manager
window = Tk()
# title for password manager #
window.title("Password Manager v1.0")

# padding for image
window.config(padx=80, pady=50)

# canvas dimensions for window of the GUI #
canvas = Canvas(height=200, width=200)

# logo image
logo_img = PhotoImage(file="shield.png")

# this will create image in canvas and its size (x and y)
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(row=0, column=1)

# Labels #
# The grid is used to section the labels into the right place in the GUI #
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)

emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)

passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3, column=0)

# Entries. Some entries will have different widths. This is the box the user will type in #
websiteEntry = Entry(width=35)
emailEntry = Entry(width=35)
passwordEntry = Entry(width=35)

# layout of Entries. This will position the entries into the proper rows and columns
websiteEntry.grid(row=1, column=1, columnspan=2)
emailEntry.grid(row=2, column=1, columnspan=2)
passwordEntry.grid(row=3, column=1, columnspan=2)

# Buttons #

# This is the add button. when the user presses add, it will trigger the save function, and save their password in a data.txt file #
addButton = Button(text="Add", width=36, command=save)
# This is the position of the add butotn #
addButton.grid(row=4, column=1, columnspan=2)

# Get the cursor to appear on the website by using websiteEntry variable and the focus method #
websiteEntry.focus()

# Starting value for email entry #
# This is to automatically populate a common email that you use for your passwords to save you time #
emailEntry.insert(0, "johndoe@email.com")



window.mainloop()
