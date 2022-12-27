from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# Generate a random password by choosing a combination of letters, numbers, and symbols
# from predefined lists, shuffling them, and joining them into a string
def generate_password():
    # Define lists of letters, numbers, and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Choose a random number of letters, symbols, and numbers
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    # Concatenate the chosen elements into a single list
    password_list = password_letters + password_symbols + password_numbers

    # Shuffle the list
    shuffle(password_list)

    # Join the list elements into a single string
    random_password = "".join(password_list)

    # Insert the password into the password input field and copy it to the clipboard
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)
    messagebox.showinfo(title="Password Copied", message="Password copied successfully!")

# Save the entered website, username, and password information to a text file if the
# website and password fields are not empty. Check with the user before saving the data.
def save_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Check if the website and password fields are not empty
    if len(website)!= 0 and len(password) != 0:
        # Ask the user if it is okay to save the entered data
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered :\nEmail/Username: {username}\nPassword:{password}\nIs it okay to save?")
        if is_ok == True:
            # Save the data to the text file
            with open("data.txt", "a") as file:
                file.write            (f"{website} | {username} | {password}\n")

            # Clear the input fields
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        # Show a warning if the website or password fields are empty
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")

# Set up the Tkinter GUI
window = Tk()
window.title("Password Manager")
window.config(width=500, height=500, padx=20,pady=20)

# Create a canvas to display the logo image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1)

# Create a label and an input field for the website
website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)
website_label.focus()

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

# Create a label and an input field for the username
username_label = Label(text="Email/Username: ")
username_label.grid(row=2,column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "insertemailhere")

# Create a label and an input field for the password
password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)

password_input = Entry(width=28)
password_input.grid(row=3, column=1)

# Create a button to generate a random password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Create a button to save the entered data
save_button = Button(text="Save", command=save_data, width=36)
save_button.grid(row=4, column=1)

# Run the main loop
window.mainloop()

