

import logging

from testGenerator import QuizGenerator

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

sample_quiz = ('\n\nQ1. What is the syntax for declaring a variable in Python?\nA. #variable\nB. var variable\nC. !variable\n'
               'D. var = variable\nCorrect Answer: D. var = variable\n\nQ2. What type of language is Python?'
               '\nA. Interpreted\nB. Compiled\nC. Assembly\nD. Machine\nCorrect Answer: A. Interpreted\n\nQ3. What type of loop is used when a set of instructions need to be repeated until a condition is met?'
               '\nA. For loop\nB. While loop\nC. Do-while loop\nD. If-else loop\nCorrect Answer: B. While loop\n\nQ4. What is the result of the following expression?'
               '\n2 + 5 * 3\nA. 23\nB. 17\nC. 11\nD. 25\nCorrect Answer: B. 17')


class Instructor:
    def init(self):
        print("Welcome! Run generate_complete_quiz() to create a quiz.")

    def generate_complete_quiz(self):

        subject = input("What subject would you like to create a quiz on? ")
        option_count = int(
            input("How many answer choices would you like to have? "))
        question_count = int(
            input("How many questions would you like to have? "))

        self.quiz_generator = QuizGenerator(subject, option_count, question_count)
        quiz = self.quiz_generator.run()
        # quiz = sample_quiz
        # logging.info(quiz)
        student_perspective = self.create_student_perspective(
            quiz, question_count)
        correct_answers = self.obtain_correct_answers(quiz, question_count)
        return student_perspective, correct_answers

    def create_student_perspective(self, quiz, question_count):
        student_perspective = {1: ""}
        current_question = 1
        for line in quiz.split("\n"):
            if not line.startswith("Correct Answer:"):
                student_perspective[current_question] += line + "\n"
            else:

                if current_question < question_count:
                    current_question += 1
                    student_perspective[current_question] = ""
        return student_perspective

    def obtain_correct_answers(self, quiz, question_count):
        answer_list = {1: ""}
        current_question = 1
        for line in quiz.split("\n"):
            if line.startswith("Correct Answer:"):
                answer_list[current_question] += line + "\n"

                if current_question < question_count:
                    current_question += 1
                    answer_list[current_question] = ""
        return answer_list



if __name__ == "__main__":
    instructor = Instructor()
    student_perspective, correct_answers = instructor.generate_complete_quiz()