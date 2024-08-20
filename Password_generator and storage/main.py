import tkinter
import random
import pandas
from password import pas
from tkinter import messagebox

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("PassWord Manager")
canvas=tkinter.Canvas(width=600,height=500,background="white")

image=tkinter.PhotoImage(file="./logo.png")


canvas.create_image(300,170,image=image)

canvas.create_text(100,310,text="Website:   ",font=("Arial",12,"normal"))
canvas.create_text(100,340,text="Email / UserName:   ",font=("Arial",12,"normal"))
canvas.create_text(100,370,text="Password:   ",font=("Arial",12,"normal"))

web_input=tkinter.Entry(width=50,borderwidth=2)
web_input.focus()
email_input=tkinter.Entry(width=50,borderwidth=2)
pass_input=tkinter.Entry(width=25,borderwidth=2)

web_input.place(x=180,y=300)
email_input.place(x=180,y=330)
pass_input.place(x=180,y=360)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web=web_input.get()
    email=email_input.get()
    pass1=pass_input.get()

    if len(web)==0 or len(pass1)==0 or len(email)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        q=messagebox.askokcancel(title="Entries",message=f"These are the details    entered:\nWebsite: {web}\nEmail: {email}\nPassword: {pass1}")
        if q:
            with open("data.txt",mode="a") as f:
                f.write("\n"+web+",")
                f.write(email+",")
                f.write(pass1)

            web_input.delete(0,tkinter.END)
            email_input.delete(0,tkinter.END)
            pass_input.delete(0,tkinter.END)

add_button=tkinter.Button(text="Add",width=42,borderwidth=3,command=add)
add_button.place(x=180,y=395)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    text1=""
    for _ in range(0,10):
        text1+=random.choice(pas)
    pass_input.delete(0,tkinter.END)
    pass_input.insert(0,text1)

gen_button=tkinter.Button(text="Generate Password",borderwidth=3,command=generate)
gen_button.place(x=373,y=360)
# ---------------------------- Show Passwords ------------------------------- #

def show():
    data=pandas.read_csv("data.txt")
    print(data)

show_pass=tkinter.Button(text="Show Passwords",width=42,borderwidth=3,command=show)
show_pass.place(x=180,y=430)

# -------------------------------------------------------------------------- #

canvas.pack()
window.mainloop()