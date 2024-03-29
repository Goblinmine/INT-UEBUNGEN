class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def human_years(self):
        years = self.age * 7
        return years 

    def walk(self):
        print(self.name, 'is walking')

    def __str__(self):
        return "I'm a dog named " + self.name

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        if self.is_working:
            print(self.name,'is helping its handler', 
                  self.handler, 'walk')
        else:
            Dog.walk(self)

    def bark(self):
        if self.is_working:
            print(self.name, 'says, "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)

class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "I'm a " + self.color + ' frisbee'

class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(self.name,
                    'says, "I can\'t bark, I have a frisbee in my mouth"')
        else:
            Dog.bark(self)

    def walk(self):
        if self.frisbee != None:
            print(self.name, 'says, "I can\'t walk, I\'m playing Frisbee!"')
        else:
            Dog.walk(self)
                    
    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'caught a', frisbee.color, 'frisbee')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'gives back', frisbee.color, 'frisbee')
            return frisbee
        else:
            print(self.name, "doesn't have a frisbee")
            return None

    def __str__(self):
        str = "I'm a dog named " + self.name
        if self.frisbee != None:
            str = str + ' and I have a frisbee'
        return str

class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'Says, "Meow"')
        
class Person():
    def __init__(self, name) -> None:
        if type(name) is not str:
            raise TypeError("param should be a string")
        self.name = name
        
class Dog_walker(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def walk_dogies(self, dogies: dict[str, Dog]) -> None:
        for dog_name, dog in dogies.items():
            dog.walk()
            
class Hotel:
    
    dog_walker: Dog_walker = None
        
    def __init__(self, name):
        self.name = name
        self.kennel_names = []
        self.kennel_dogs = []
        self.kennel = {}

    def check_in(self, dog):
        if isinstance(dog, Dog):
             self.kennel[dog.name] = dog
             print(dog.name, 'is checked into', self.name)
        else:
             print('Sorry only Dogs are allowed in', self.name)

    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        else:
            print('Sorry,', name, 'is not boarding at', self.name)
            return None

    def barktime(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()
            
            
    def hire_dog_walker(self, dog_walker: Dog_walker) -> None:
        if type(dog_walker) is not Dog_walker:
            raise TypeError("param should be a Dog_walker")
              
        self.dog_walker = dog_walker 
        
    
    def walk_service(self) -> None:
        if self.dog_walker == None:
            print('No Dogwalker hired!')
            return
        self.dog_walker.walk_dogies(self.kennel)

def test_code():
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    # frisbee = Frisbee('red')
    # dude =  FrisbeeDog('Dude', 5, 20)
    # dude.catch(frisbee)

    # codie.walk()
    # jackson.walk()
    # rody.walk()
    # dude.walk()
    
    hans = Dog_walker('Hans')
    hotel = Hotel('HHH')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(rody)
    # hotel.hire_dog_walker(hans)
    hotel.walk_service()

test_code()
