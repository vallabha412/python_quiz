""" Main script. """
from quiz_brain import QuizBrain
from data import question_data

quiz = QuizBrain(question_data)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
