# import req

# response=requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
# print(response.json())

# def fun1(num:int):
#     res=num *6
#     return res
# print(fun1('2')

# def fun(num:int):
#     if num>18:
#         print("yes")
#     else:
#         print("no")
# fun("char")

# def greet()-> str:
#     return 1

# print(greet())
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question.text)
print(question_bank)