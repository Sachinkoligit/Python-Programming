from question_model import question
from data import question_data
from quiz_brain import quizbrain

question_bank=[]
for item in question_data:
  q=question(item["question"],item["correct_answer"])
  question_bank.append(q)

quiz=quizbrain(question_bank)
while quiz.question_left():
  quiz.next_question()
print("You've completed the quiz.")  
print(f"Your final score is: {quiz.score}/{quiz.question_number}")