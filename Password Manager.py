from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# -------------------------------Password Generator-----------------------------------
from random import randint,choice,shuffle

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # password_list = []
    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for j in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #     password += char
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")
# -------------------------------SAVE PASSWORD --------------------------------------


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!!', message='Do not leave any field empty!!')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading the old data
                data = json.load(data_file)

        except:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating the old data with the new data
            data.update(new_data)
            # Saving the updated data
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_website():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
           data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Such Data File Found!')

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.askokcancel(title=website, message=f'Email: {email}\nPassword: {password}\nClick Ok to insert '
                                                          f'the password!')
            password_entry.insert(END, password)
        else:
            messagebox.showinfo(title='ERROR', message=f'No emails and passwords for {website} website exists!')


# --------------------------------UI SETUP--------------------------------------------


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
logo = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username: ')
email_label.grid(row=2, column=0,pady=10)

password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'sahilshah0620@gamil.com')

password_entry = Entry(width=21, show='*')
password_entry.grid(row=3, column=1)

generate_password = Button(text='Generate Password', command=password_generator)
generate_password.grid(row=3, column=2)

add = Button(text='Add', width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=search_website, width=13)
search_button.grid(row=1,column=2)
window.mainloop()


# Searching for a website in the password manager.







