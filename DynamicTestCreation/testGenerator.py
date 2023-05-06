import os

import openai



class QuizGenerator:
    def init(self, topic, option_count, question_count):
            
            self.topic = topic
            self.option_count = option_count
            self.question_count = question_count

            if self.question_count > 6:
                 raise ValueError("Attention! Generating a large number of questions might be expensive!")
            if self.option_count > 5:
                 raise ValueError("More than 5 answer choices are not supported!")

    def run(self):
        prompt = self.construct_prompt()
        if QuizGenerator._confirm_prompt(prompt):
            response = self.create_quiz(prompt)
            return response["choices"][0]["text"]
        
        raise ValueError("Prompt not accepted.")

    def create_quiz(self, prompt):
        openai.api_key = os.environ["OPENAI_API_KEY1"]
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt=prompt,
                                            max_tokens=256,
                                            temperature=0.7)

        return response

    @staticmethod
    def _confirm_prompt(prompt):
        print(prompt)
        user_response = input("Are you satisfied with the prompt? (y/n)")

        if user_response.upper() == "Y":
            return True
        return False

    def construct_prompt(self):
        prompt = (f"Generate a multiple-choice quiz on the topic of {self.topic} with {self.question_count} questions. "
                f"Provide {self.option_count} options for each question. "
                f"Include the correct answer for each question, starting with 'Correct Answer: '.")
        return prompt


if __name__ == "__main__":
    generator = QuizGenerator("Python", 4, 2)
    quiz = generator.run()
    print(quiz)