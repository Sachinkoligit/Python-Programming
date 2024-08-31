BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas
import random
import time
# *********************************UI-SetUp***************************************

window=tkinter.Tk("blue")
window.minsize(width=800,height=520)
canvas=tkinter.Canvas(height=650,width=900,background=BACKGROUND_COLOR)
back_img=tkinter.PhotoImage(file="./images/card_front.png")
front_img=tkinter.PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(450,280,image=back_img)

right_img=tkinter.PhotoImage(file="./images/right.png")
left_img=tkinter.PhotoImage(file="./images/wrong.png")

title=canvas.create_text(450,150,text="French",font=("Ariel",40,"italic"))
word=canvas.create_text(450,263,text="Word",font=("Ariel",60,"bold"))

#********************************Reading csv file*************************

try:
    pandas.read_csv("./data/unknown_french_words.csv")
except:
    with open("./data/unknown_french_words.csv",mode='w') as file1:
        pass
    content=pandas.read_csv("./data/french_words.csv")
else:
    content=pandas.read_csv("./data/unknown_french_words.csv")

new_dict=content.to_dict(orient="records")

def left_random_word():
    global french_word,x
    x=random.choice(new_dict)
    french_word=x["French"]
    english_word=x["English"]
    canvas.itemconfig(word,text=french_word)
    timer=window.after(3000,flip,english_word)
    # window.after_cancel(timer)
    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,fill="black")

left_button=tkinter.Button(image=left_img, highlightthickness=0,command=left_random_word)
left_button.place(x=650,y=540)

def right_random_word():
    try:
        new_dict.remove(x)
        y=pandas.DataFrame(new_dict)
        y.to_csv("./data/unknown_french_words.csv",index=False)
    except:
        pass
    finally:
        left_random_word()

right_button=tkinter.Button(image=right_img, highlightthickness=0,command=right_random_word)
right_button.place(x=150,y=540)

#***************************Flip Card*****************************
def flip(en):
    canvas.itemconfig(canvas_image,image=front_img)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=en,fill="white")

#*************************Save Progress****************************

canvas.pack()
window.title("Flash_Card")
window.mainloop()