class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {current_question.text} ")
        # next line is just a hint to check if the code works correctly
        print("***hint : the correct answer is : ", current_question.answer , "***")

        user_answer=input("t , true , y , yes for True \nAnd f , false , n and no for False : \n"   )
        if user_answer == "True" or user_answer == "t" or user_answer == "T" or user_answer == "y" or user_answer == "yes":
            user_answer = "True"
        if user_answer == "False" or user_answer == "f" or user_answer == "F" or user_answer == "no" or user_answer=="n":
            user_answer = "False"
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
