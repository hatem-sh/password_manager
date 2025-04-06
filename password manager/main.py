from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
YELLOW = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    the_website = website_input.get()
    the_username = username_input.get()
    the_password = password_input.get()
    new_data = {
        the_website: {
            "email": the_username,
            "password": the_password,
        }
    }

    if the_website == "":
        messagebox.showerror(title="Error", message="you should fill up all the fields!")

    elif the_username == "":
        messagebox.showerror(title="Error", message="you should fill up all the fields!")

    elif the_password == "":
        messagebox.showerror(title="Error", message="you should fill up all the fields!")

    else:

        try:
            with open("file.json", "r") as f:
                # reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # updating oid data with new one
            data.update(new_data)

            with open("file.json", "w") as f:
                # saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------  Password search ------------------------------- #


def find_password():
    needed_website = website_input.get()
    try:
        with open("file.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:

        messagebox.showinfo(title="Error", message="there is no file found")

    try:
        needed_email = data[needed_website]["email"]
        needed_password = data[needed_website]["password"]
        messagebox.showinfo(title="info", message=f"Email: {needed_email}\n"
                                                  f"Password: {needed_password}\n\n\nThe password is copied already ")
        print(data[needed_website])
        pyperclip.copy(f"{needed_password}")

    except KeyError:
        messagebox.showerror(title="Error", message=f"there is no such website called: '{needed_website}'")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username", font=("Arial", 12, "bold"))
username_label.grid(row=2, column=0)

password_label = Label(text="password", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)


website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)

username_input.insert(0, "hatem@gmail.com")


password_input = Entry(width=30)
password_input.grid(row=3, column=1)

create_button = Button(text="   Create  ", command=create)
create_button.grid(column=2, row=3)
create_button.config(command=create)

# password add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(command=save)

# search button
search_button = Button(text="   Search  ", command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
