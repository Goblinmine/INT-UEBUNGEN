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



my_queue = Queue()
my_queue.enqueue("first item")
print(f"Queue: {my_queue}")
print(f"Queue emty?: {my_queue.is_empty()}")
my_queue.enqueue("second item")
print(f"Queue: {my_queue}")
print(f"Queue dequeue: {my_queue.dequeue()}")
print(f"Queue: {my_queue}")
print(f"Queue dequeue: {my_queue.dequeue()}")
print(f"Queue: {my_queue}")
print(f"Queue emty?: {my_queue.is_empty()}")

my_stack = Stack()
my_stack.push("first item")
print(f"Stack: {my_stack}")
print(f"Stack emty?: {my_stack.is_empty()}")
my_stack.push("second item")
print(f"Stack: {my_stack}")
print(f"Stack pop: {my_stack.pop()}")
print(f"Stack: {my_stack}")
print(f"Stack pop: {my_stack.pop()}")
print(f"Stack: {my_stack}")
print(f"Stack emty?: {my_stack.is_empty()}")