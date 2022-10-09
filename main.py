from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# save details
def save():
    website = entry1.get()
    mail = entry2.get()
    password = entry3.get()
    if website=="" or password== "":
        messagebox.showerror(title="Error", message="Please fill the blank spaces")
    else:
        is_ok =messagebox.askokcancel(title=website, message=f"these are the details entered Email: {mail} ,Password : {password}. Is this ok to save?")
        if is_ok:
            data_file= open("data.txt","a")
            data_file.write(f"{website} , {mail} ,  {password} \n")
            entry1.delete(0, END)
            entry3.delete(0,END)

#RANDOM PASSWORD GENERATOR
def password():
    letters= ["a", 'b','c', 'd', 'e', 'f', 'g', 'l']
    numbers= ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
    symbols= ['!','#', '$', '%', '*', '¬', '^']

    password_letter= [choice(letters) for _ in range(randint(5, 6))]
    passord_symbol= [choice(symbols) for _ in range(randint(2, 4))]
    passord_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list= password_letter + passord_symbol + passord_number
    shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

# UI
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, background="cyan")
photo = ImageTk.PhotoImage(Image.open("lock.png"))
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, columnspan=2)

label1 = Label(text="Website")
label1.grid(row=1, column=0)

label2 = Label(text="Email")
label2.grid(row=2, column=0)

label3 = Label(text="Password")
label3.grid(row=3, column=0)

entry1 = Entry(width=35)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()

entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0, "xyz@gmail.com")

entry3 = Entry(width=15)
entry3.grid(row=3, column=1, columnspan=2)
entry3.place(x=57, y=242)

Generate_password = Button(text="Generate Password", command= password)
Generate_password.grid(row=3, column=2)
Generate_password.place(x=160, y=238)

add_button = Button(text="Add", width=15, command=save)
add_button.grid(row=4, column=1, columnspan=2)
add_button.place(x=100, y=270)

window.mainloop()
