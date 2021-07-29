from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    text = x["text"]
    answer = x["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)
print(question_bank[0].text)

quize = QuizBrain(question_bank)

while True:
    check = quize.check_remain()

    if check == False:
        break
    quize.next_question()
print(f"Thank you Total you got {quize.score} point")

