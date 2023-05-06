import os
from aiTestInstructor import Instructor

from quizSimultor import Quiz
os.environ["OPENAI_API_KEY1"] = "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"  # gayatri's key
instruction = Instructor()

student_perspective, correct_answers = instruction.generate_complete_quiz()

quiz = Quiz(student_perspective, correct_answers, save_quiz=False, topic= instruction.quiz_generator.topic)
get_student_answers = quiz.participate()
print(get_student_answers)
evaluation_results = quiz.evaluate(get_student_answers)
print(evaluation_results)