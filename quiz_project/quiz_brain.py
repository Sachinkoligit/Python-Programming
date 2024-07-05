class quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    
    def next_question(self):
       current_question=self.question_list[self.question_number]
       self.question_number+=1
       x=input(f"{self.question_number}: {current_question.question} (True/False): ")
       self.check(x,current_question.answer)

    def question_left(self):
        return self.question_number<len(self.question_list)
    
    def check(self,x,y):
        if x==y:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {y}")
        print(f"Your Current score is: {self.score}/{self.question_number}\n")