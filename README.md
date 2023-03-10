<h1>Password Manager App with Built-in Password Generator</h1>

<p>This is a simple Python app that serves as a password manager. It allows you to save your login information for various websites, including the website URL, your email or username, and your password. The app also includes a feature to generate random passwords, which can be useful if you want to create a new password for a website but are having trouble coming up with one on your own. The app has a GUI built with Tkinter that makes it easy to use, and it saves your login information to a text file for easy access later.</p>

<h2>Prerequisites</h2>

<p>To use this script, you will need to have Python installed on your machine. You will also need to install the following Python package:</p>

<ul>
  <li>pyperclip</li>
</ul>
<p>Tkinter and the Random package are pre-installed with python</p>
<p>You can install this package using <code>pip</code>, the Python package manager. To install the <code>pyperclip</code> package, you can run the following command:</p>

<pre>
pip install pyperclip
</pre>

<h2>How to Use</h2>

<p>To use the script, simply run it in your Python environment. A GUI will appear with three input fields: one for the website, one for the username, and one for the password. To generate a new password, click the "Generate Password" button. The generated password will be displayed in the password field and copied to your clipboard. You can then paste the password into the login form for the website.</p>

<p>To save the login information, enter the website and username into the appropriate fields and click the "Save Data" button. The script will ask you to confirm that you want to save the data before doing so. The data will be saved to a text file named "data.txt" in the same directory as the script.</p>

<h2>Customization</h2>

<p>You can customize the script by modifying the lists of letters, numbers, and symbols that are used to generate the password. Simply edit the <code>letters</code>, <code>numbers</code>, and <code>symbols</code> variables at the top of the script to include the characters that you want to use. You can also adjust the number of letters, symbols, and numbers that are included in the generated password by modifying the <code>randint</code> function calls in the <code>generate_password</code> function.</p>

<h2>Notes</h2>

<ul>
  <li>The "data.txt" file is created if it does not already exist.</li>
  <li>If you want to clear the input fields, you can simply click on them and press the "Backspace" or "Delete" key on your keyboard.</li>
  <li>The password is generated by choosing a random number of letters, symbols, and numbers from predefined lists and shuffling them. The resulting password is not guaranteed to be secure, but it should be sufficient for most casual use cases.</li>
</ul>

<h2>Tutorial</h2>

<h3>Importing the necessary modules</h3>

<p>The first step is to import the necessary modules. We will be using the following modules:</p>

<ul>
  <li><code>random</code> for generating random numbers and selecting random elements from lists</li>
  <li><code>pyperclip</code> for copying the generated password to the clipboard</li>
</ul>
<p>To import these modules, add the following lines to the top of your script:</p>
<pre>
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
</pre>
<h3>Defining the generate_password function</h3>
<p>The <code>generate_password</code> function is responsible for generating a random password. It does this by defining lists of letters, numbers, and symbols, and then choosing a random number of elements from each list. The chosen elements are shuffled and joined into a single string to create the password. The password is then inserted into the password input field and copied to the clipboard. Finally, a message box is displayed to confirm that the password has been copied.</p>
<p>To define the <code>generate_password</code> function, add the following block of code to your script:</p>
<pre>
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
</pre>
<h3>Defining the save_data function</h3>
<p>The <code>save_data</code> function is responsible for saving the website, username, and password information to a text file. It first checks that the website and password fields are not empty, and then asks the user to confirm that they want to save the data. If the user confirms, the data is written to the "data.txt" file in the same directory as the script. Finally, the input fields are cleared.</p>

<p>To define the <code>save_data</code> function, add the following block of code to your script:</p>
<pre>
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
                file.write(f"{website} | {username} | {password}\n")
        # Clear the input fields
            website_input.delete(0, END)
password_input.delete(0, END)
else:
        # Show a warning if the website or password fields are empty
messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")
</pre>

<h3>Setting up the GUI with Tkinter</h3>
<p>Next, we will set up the GUI for the script using Tkinter. First, we will create a new window and add a label and input field for the website. Then, we will add a label and input field for the username. Finally, we will add a label and input field for the password, as well as a "Generate Password" button and a "Save Data" button. You can customize the layout and appearance of the GUI by modifying the arguments passed to the various Tkinter functions.</p>
<p>To set up the GUI, add the following block of code to your script:</p>
<pre>
# Create a new window
window = Tk()
window.title("Password Generator")

# Create a canvas to display the logo image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Add a label and input field for the website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=40)
website_input.grid(row=1, column=1)

# Add a label and input field for the username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_input = Entry(width=40)
username_input.grid(row=2, column=1)


# Add a label and input field for the password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=40)
password_input.grid(row=3, column=1)

# Add a button to generate a new password
generate_password_button = Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=0, sticky=W)

# Add a button to save the data
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=0)

# Run the main loop
window.mainloop()
</pre>

<h2>Conclusion</h2>
<p>In conclusion, this is a useful tool for managing your passwords and keeping track of your login information for various websites. The app's GUI makes it easy to use, and the ability to generate random passwords can be a helpful feature if you want to create a new password but are having trouble coming up with one on your own. By modifying the lists of letters, numbers, and symbols used to generate the passwords, as well as the layout and appearance of the GUI, you can customize the app to suit your needs. Whether you're looking to improve your password security or simply want a convenient way to keep track of your login information, this app is a great choice.If you have any questions or need further assistance, feel free to ask.</p>
