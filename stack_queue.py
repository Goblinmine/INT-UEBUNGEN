class Stack:
    
    __liste: list
    
    def __init__(self):
        self.__liste = []
        
    def __str__(self) -> str:
        return str(self.__liste)
    
    def pop(self):
        return self.__liste.pop()

        
    def push(self, obj: any):
        self.__liste.append(obj)
           
    
    def is_empty(self):
        return True if len(self.__liste) == 0 else False

class Queue:
    __liste: list
    
    def __init__(self):
        self.__liste = []
        
    def __str__(self) -> str:
        return str(self.__liste)
    
    def enqueue(self, obj: any):
        self.__liste.append(obj)
    
    def dequeue(self):
        return self.__liste.pop(0)
    
    def is_empty(self):
        return True if len(self.__liste) == 0 else False
    
