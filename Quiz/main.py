from quiz_brain import Quiz
from data import question_data

# Q.1: The HTML5 standard was published in 2014. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 1/1


def main():
    quiz = Quiz(question_data)
    
    def get_user_input(input_str: str) -> bool:
        
        output = None
        while output == None:
            user_input = input(input_str).lower()
            if user_input in ('true', 't', '1'):
                output = True
            elif user_input in ('false', 'f', '0'):
                output = False
            else:
                print("\nInput Error! Try again. Press ctrl + c to exit.\n")
                
        return output
    
    while not quiz.completed:
        next_question = quiz.get_next_question()
        result = quiz.answer_question(get_user_input(f"Q.{next_question[0]}: {next_question[1]} (True/False): "))
        
        print("You got it right!" if result[0] else "That's wrong.")
        print(f"The correct answer was: {result[1]}")
        print(f"You'r current score is: {quiz.score()}\n")
        
    if quiz.completed:
        print(f"You've completed the quiz\nYour final score was: {quiz.score()}")

main()