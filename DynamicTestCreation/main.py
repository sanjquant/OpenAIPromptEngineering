import os
from aiTestInstructor import Instructor

from quizSimultor import Quiz
instruction = Instructor()

student_perspective, correct_answers = instruction.generate_complete_quiz()

quiz = Quiz(student_perspective, correct_answers, save_quiz=False, topic= instruction.quiz_generator.topic)
get_student_answers = quiz.participate()
print(get_student_answers)
evaluation_results = quiz.evaluate(get_student_answers)
print(evaluation_results)