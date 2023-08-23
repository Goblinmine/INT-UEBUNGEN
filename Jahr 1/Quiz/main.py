from quiz_brain import Quiz
from data import question_data
import urllib.request
import json
import base64

URL = 'https://opentdb.com/api.php?amount=12&type=boolean&encode=base64'

# README!!!
# if you want to use this with the data.py questions insted of the API set the use_api variable to False!
use_api = True


def main():
    def question_data_api():
        response = urllib.request.urlopen(URL)
        data = json.loads(response.read().decode())           
        return [{"text":base64.b64decode(x['question']).decode(), "answer":base64.b64decode(x['correct_answer']).decode()} for x in data['results']]
    
    def get_user_input(input_str: str) -> bool:
        output = None
        while output == None:
            user_input = input(input_str).lower()
            if user_input in ('true', 't', '1'): output = True
            elif user_input in ('false', 'f', '0'): output = False
            else: print("\nInput Error! Try again. Press ctrl + c to exit.\n")
                
        return output
    
    quiz = Quiz(question_data_api() if use_api else question_data)   
    
    while not quiz.completed:
        next_question = quiz.get_next_question()
        result = quiz.answer_question(get_user_input(f"Q.{next_question[0]}: {next_question[1]} (True/False): "))
        
        print("You got it right!" if result[0] else "That's wrong.")
        print(f"The correct answer was: {result[1]}")
        print(f"You'r current score is: {quiz.score()}\n")
        
    if quiz.completed:
        print(f"You've completed the quiz\nYour final score was: {quiz.score()}")

main()