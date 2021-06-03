from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while not new_quiz.still_has_question():
    new_quiz.next_question()
    print()

print("You have completed the quiz!!")
print(f"Your final score is: {new_quiz.score}/{new_quiz.question_number}.")
