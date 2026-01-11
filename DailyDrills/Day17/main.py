from Day17.quizbrain import QuizBrain
from data import question_data
from question_model import Question

# Creating the objects here
question_bank = []

user_input = input("Hello ")
question_number = 0
quiz = QuizBrain(question_number, user_input)

index = 0
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    question = Question(q_text, q_answer)
    question_bank.append(question)


print(question_bank)
