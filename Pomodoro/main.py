import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_label,text="00:00")
    title.config(text="Timer")
    label_tick.config(text="")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count(num):
    min=num//60
    second=num%60
    if second<10:
        second=f"0{second}"
    canvas.itemconfig(timer_label,text=f"{min}:{second}")
    if(num>0):
        global timer
        timer=window.after(1000,count,num-1)
    else:
        run()
        text=""
        for _ in range(0,reps//2):
            text+="✔"
        label_tick.config(text=text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def run():
    global reps
    
    if reps==7:
        title.config(text="Break_Time",fg=RED)
        count(20*60)
        reps+=1
    elif reps%2!=0:
        title.config(text="Break_Time",fg=PINK)
        count(5*60)
        reps+=1
    elif reps>7:
        window.after_cancel(timer)
    else :
        title.config(text="Work_Time",fg=GREEN)
        count(25*60)
        reps+=1

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.minsize(height=400,width=500)
window.title("POMODORO")
canvas=tkinter.Canvas(width=500,height=400,background=YELLOW)
image1=tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(250,200,image=image1)
label_tick=tkinter.Label(text="",fg=GREEN,bg=YELLOW,font=("Arial",20))
label_tick.place(x=250,y=350)
timer_label=canvas.create_text(250,220,text="00:00",font=(FONT_NAME,20,"bold"),fill="white")
title=tkinter.Label(text="Timer",font=(FONT_NAME,40,"normal"),fg=GREEN,bg=YELLOW)
title.place(x=150,y=20)
canvas.pack()
button_start=tkinter.Button(text="Start",padx=10,command=run).place(x=110,y=300)
button_reset=tkinter.Button(text="Reset",padx=10,command=reset).place(x=330,y=300)
window.mainloop()