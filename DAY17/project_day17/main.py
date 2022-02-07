from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    text = question['text']
    answer = question['answer']
    n = Question(text,answer)
    question_bank.append(n)

q = QuizBrain(question_bank)
# q.question_number-=1

while q.still_has_questions():
    q.next_question()


print("You have completed the quiz")
print(f"Your final score was: {q.score}/{q.question_number}")