from question_model import Question

class Quiz:
    __questions: list[Question] = []
    __score: int = 0
    __current_position: int = 0
    completed = False
    
    def __init__(self, quiz_data: list[dict[str, str]] = None) -> None:

        
        if quiz_data is not None:
            for question_data in quiz_data:
                self.__questions.append(Question(question_data))
                
    # def import_quiz_data(self, quiz_data) -> bool:
    #     """Imports quiz data if not allready done on init"""
    #     if len(self.__questions) == 0:
    #         return False
        
    #     for question_data in quiz_data:
    #             self.__questions.append(Question(question_data))  
                
    #     return True 
         
    def get_next_question(self) -> tuple[str, str]:
        """Retuns score and next question"""
        
        self.__current_position += 1
        return f"{self.__current_position}", self.__questions[self.__current_position -1].txt
    
    def answer_question(self, user_input: bool) -> tuple[bool, str]:
        """Checks if answer is correct.
        Returns if correct and what would be correct"""
        
        output = False
        if user_input == self.__questions[self.__current_position -1].answer:
            output = True
            self.__score += 1
        
        if self.__current_position == len(self.__questions): self.completed = True
        return output, str(self.__questions[self.__current_position -1].answer)
        
               
    def score(self) -> str:
        """Returns string of score -> \"1/3\""""
        return f"{self.__score}/{self.__current_position}"
    
    # resets the scores       
    def restart(self):
        """Resets all scores and counters for a new game"""
        self.completed = False
        self.__score = 0
        self.__current_position = 0
        