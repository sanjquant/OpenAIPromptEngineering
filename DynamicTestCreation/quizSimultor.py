import datetime

from aiTestInstructor import Instructor

class Quiz:
    def init(self, student_perspective, correct_answers, save_quiz=False, topic=""):
        self.student_perspective = student_perspective
        self.correct_answers = correct_answers

        if save_quiz:
            self.save_quiz(topic)

    def participate(self):
        submitted_answers = {}
        for question_num, question_content in self.student_perspective.items():
            print(question_content)
            response = input("Enter your answer: ")
            submitted_answers[question_num] = response
        return submitted_answers

    def evaluate(self, submitted_answers):
        accurate_responses = 0
        for question_num, response in submitted_answers.items():
            if response.upper() == self.correct_answers[question_num].upper()[16]:
                accurate_responses += 1
        score = 100 * accurate_responses / len(submitted_answers)

        if score < 60:
            pass_status = "Not passed!"
        else:
            pass_status = "Passed!"
        return f"{accurate_responses} out of {len(submitted_answers)} correct! You achieved: {score}% : {pass_status}"

    def save_quiz(self, topic):
        with open(f'Quiz_{topic}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt', "w") as file:
            for question_num, question_content in self.student_perspective.items():
                file.write(question_content)
                file.write("\n")
                file.write(self.correct_answers[question_num])
                file.write("\n")



if __name__ == "__main__":
    instructor = Instructor()
    student_perspective, correct_answers = instructor.generate_complete_quiz()


    quiz = Quiz(student_perspective, correct_answers, save_quiz=True, topic=instructor.quiz_generator.topic)
    submitted_answers = quiz.participate()
    print(submitted_answers)
    evaluation = quiz.evaluate(submitted_answers)
    print(evaluation)
