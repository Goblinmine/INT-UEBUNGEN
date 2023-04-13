class Question:
    txt: str
    answer: bool
    
    def __init__(self, question: dict[str, str]) -> None:
        self.txt = question['text']
        self.answer = True if question['answer'] == 'True' else False