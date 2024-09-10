import tkinter,time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,height=500,width=400)
        
        self.score=tkinter.Label(text="Score: 0",bg=THEME_COLOR,font=("Arial",15,"normal"),fg="white")
        self.score.grid(row=0,column=1,padx=20,pady=20)

        self.canvas=tkinter.Canvas(height=250,width=300,background="white")
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

        self.r_image=tkinter.PhotoImage(file="./images/true.png")
        self.right_button=tkinter.Button(image=self.r_image,command=self.right_check)
        self.right_button.grid(row=2,column=0,padx=20,pady=20)

        self.w_image=tkinter.PhotoImage(file="./images/false.png")
        self.wrong_button=tkinter.Button(image=self.w_image,command=self.wrong_check)
        self.wrong_button.grid(row=2,column=1,padx=20,pady=20)
        
        self.question=self.canvas.create_text(150,125,width=280,text="Some Question Text",font=("Arial",20,"italic"),fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_check(self):
        self.feedback(self.quiz.check_answer("true")) 

    def wrong_check(self):
        self.feedback(self.quiz.check_answer("false"))
    
    def feedback(self,ch):
        if ch:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

        