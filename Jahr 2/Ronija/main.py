from typing import Any, Self
from random import Random as r

class Person():
    def __init__(self, name: str, is_male: bool, current_position: str = None, 
                 mutter: Self = None, father: Self = None, home: str = None) -> None:
        self.name = name
        self.mutter = mutter
        self.fater = father
        self.is_male = is_male
        self.home = home
        
        if current_position == None and home == None:
            raise AttributeError('current_position must be set if home is also not set')
        
        self.current_position = home if home != None and current_position == None else current_position
        self.is_hostage = False
        self.scared = False
        self.free = True
        self.__dead = False
        self.friends = []
        self.currently_with_group = True
        
    def move_to(self, ort: str) -> None:
        if self.is_hostage:
            print(f'{self.name} is a hostage so cant move on its own.')
        else:
            self.current_position = ort
            print(f'{self.name} moves to {ort}')
            
    def move_as_hostage(self, hostage_taker: Self, ort):
        if not self.is_hostage:
            print(f'{self.name} is not a hostage so can move freelie.')
        else:
            self.current_position = ort
            print(f'{hostage_taker.name} takes {self.name} to {ort}')
    
    def talk(self, msg: str) -> None:
        print(f'{self.name} says: "{msg}"')
        
    def give_birth(self, father: Self, is_male: bool, name: str) -> Self:
        if not self.is_male:
            print(f'{self.name} gave birth to {name} in {self.current_position}')
            return Person(name=name, mutter=self, father=father, is_male=is_male, 
                          home=self.home, current_position=self.current_position)
    
    def set_new_home(self, home: str) -> None:
        self.home = home
        print(f'{self.name}s new home is {home}')
        
    def add_friend(self, friend: Self) -> None:
        self.friends.append(friend)
        friend.friends.append(self)
        print(f'{self.name} is now friends with {friend.name}')
        
    def remove_friend(self, person: Self) -> None:
        self.friends.remove(person)
        person.friends.remove(self)
        print(f'{self.name} ended friendship with {person.name}')
        
    def killed(self) -> None:
        self.__dead == True
        print(f'{self.name} is now dead!')
        
    def feels(self, feels: str) -> None:
        print(f'{self.name} {feels}')
        
class Rauber(Person):
    def __init__(self, name: str, is_male: bool, current_position: str = None, 
                 mutter: Self = None, father: Self = None, home: str = None) -> None:
        super().__init__(name, is_male, current_position, mutter, father, home)
        self.hostages: list[Person] = []
    
    def take_hostage(self, person: Person) -> None:
        if person not in self.hostages:
            person.is_hostage = True
            self.hostages.append(person)
            print(f'{self.name} took {person.name} as hostage.')
        
    def release_hostage(self, person: Person = None) -> None:
        if person == None:
            print(f'{self.name} released all his hostages.')
            for hostage in self.hostages:
                hostage.is_hostage = False
            self.hostages = []
        elif person in self.hostages:
            person.is_hostage = False
            self.hostages.remove(person)
            print(f'{self.name} released {person.name}')
        
    def ich_will_kein_rauber_mehr_sein(self) -> Person:
        new_person = Person(self.name, self.current_position, self.is_male, self.mutter, self.fater, self.home)
        print(f"{self.name} doesn's want to be a Räuber anymore. Is now a normal Person.")
        return new_person
    
    def move_to(self, ort: str) -> None:
        for hostage in self.hostages:
            hostage.move_as_hostage(self, ort)
        return super().move_to(ort)
    
    def give_birth(self, father: Self, is_male: bool, name: str) -> Self:
        if not self.is_male:
            print(f'{self.name} gave birth to {name} in {self.current_position}')
            return Rauber(name=name, mutter=self, father=father, is_male=is_male, 
                          home=self.home, current_position=self.current_position)

class Gruppe():
    def __init__(self, home: str, current_position: str, 
                 name: str = None, people: list[Person] = []) -> None:
        self.home = home
        self.current_position = current_position
        self.personen: list[Person] = people
        self.in_conflict = []
        self.name = name
        
    def move_to(self, ort: str) -> None:
        for person in self.personen:
            person.move_to(ort)
        print(f'Gruppe {self.name} moved to {ort}.')
        
    def move_home(self) -> None:
        self.move_to(self.home)
        
    def start_conflict(self, group: Self) -> None:
        if group not in self.in_conflict:
            self.in_conflict.append(group)
            group.in_conflict.append(self)
            print(f'{self.name} started conflict with {group.name}')
        
    def stop_conflict(self, group: Self) -> None:
        if group in self.in_conflict:
            self.in_conflict.remove(group)
            group.in_conflict.remove(self)
            print(f'{self.name} stoped the conflict with {group.name}')
        
    def add_person(self, person: Person, quiet = False) -> None:
        self.personen.append(person)
        if not quiet: print(f"{person.name} now part of {self.name}")    
        
    def remove_person(self, person: Person) -> None:
        self.personen.remove(person)
        print(f"{person.name} got removed from {self.name}")
        
    def set_new_home(self, new_home: str) -> None:
        self.home = new_home
        print(f'{self.name} new home now {new_home}')
        
    def ambush(self, group: Self) -> None:
        print(f"{self.name} ambushed {group.name}")
        self.start_conflict(group)   
        
    def merge_gruppe(self, gruppe: Self, new_name: str) -> Self:
        output = Gruppe(self.home, self.current_position, new_name)
   
        for person in self.personen:
            output.add_person(person, True)
        for person in gruppe.personen:
            output.add_person(person, True)
            
        print(f'{self.name} and {gruppe.name} merged to new group called {new_name}')
        return output
    
class RauberBande(Gruppe):
    def __init__(self, hauptmann: Person, home: str, current_position: str, name: str = None, people: list[Rauber] = []) -> None:
        super().__init__(home, current_position, name, people)
        self.hauptmann = hauptmann
        
    def add_person(self, rauber: Rauber, quied = False) -> None:
        if not isinstance(rauber, Rauber):
            raise TypeError()
        
        return super().add_person(rauber, quied)
    
    def merge_gruppe(self, gruppe: Self, new_name: str, new_hauptmann) -> Self:        
        output = RauberBande(new_hauptmann, self.home, self.current_position, new_name)
        
        for rauber in self.personen:
            output.add_person(rauber, True)
        for rauber in gruppe.personen:
            output.add_person(rauber, True)
            
        print(f'{self.name} and {gruppe.name} merged to new group called {new_name}')
            
        return output
        
class Landsknechte(Gruppe):
    def __init__(self, lord: Person, home: str, current_position: str, name: str = None, people: list[Person] = []) -> None:
        super().__init__(home, current_position, name, people=people)
        self.lord = lord
        
# Monster

class Monster():
    def __init__(self, home: str, current_position: str) -> None:
        self.home = home
        self.current_position = current_position
        night_active: bool = None

    def move_home(self) -> None:
        self.current_position = self.home
        
class Dunkelolker(Monster):
    def __init__(self, home: str, current_position: str) -> None:
        super().__init__(home, current_position)
        
    def talk(self, msg: str) -> None:
        print(f'{self.__class__} says:"{msg}".')
        
class Unterirdischen(Monster):
    def __init__(self, home: str, current_position: str) -> None:
        super().__init__(home, current_position)
        
    def lure_human(self, person: Person) -> None:
        raise NotImplementedError()
        
class Rumpelwichte(Monster):
    def __init__(self, home: str, current_position: str) -> None:
        super().__init__(home, current_position)
        
    def tripping_hayard(self, person: Person) -> None:
        raise NotImplementedError()
    
class Graugnome(Monster):
    def __init__(self, home: str, current_position: str) -> None:
        super().__init__(home, current_position)
        self.night_active = True
        
    def call_kin(self, ammount = 10) -> None:
        raise NotImplementedError()
    
class Wildruden(Monster):
    def __init__(self, home: str, current_position: str) -> None:
        super().__init__(home, current_position)
        self.child_in_fangs: Person = None
        self.night_active = False
        
    def abduct_kill_human_child(self, child: Person) -> None:
        raise NotImplementedError()
    
    def __kill_human(self) -> None:
        if self.child_in_fangs == None:
            print('I cant kill. i dont have a child in my fangs.')
        elif self.current_position != self.home:
            print('I cant kill the child here. I need to fly home.')
        else:
            self.child_in_fangs.killed()
            
class EncounterController():
    def __init__(self) -> None:
        self.moster: list[Monster] = None
        self.__create_monster_pool()
        
    def trigger_encounter(person: Person) -> Monster:
        raise NotImplementedError()
    
    def __create_monster_pool(self):
        pass
        # r.randint(10)

        
def main():
    encounter = EncounterController()
    
    lars = Person(name='Lars', is_male=True, current_position='Mattiswald')
    ludwig = Person(name='Ludwig', is_male=True, current_position='Mattiswald')
    leroy = Person(name='Leroy', is_male=True, current_position='Mattiswald')
    
    landsknechte = Landsknechte(Person(name='Vog', is_male=True, home='Vogts Castle'), 
                                'Mattiswald', 'Mattiswald', 'Landsknechte des Vogts', people=[lars, ludwig, leroy])
    
    mattis = Rauber(name='Mattis', is_male=True, home='Mattisburg')
    lovis = Rauber(name='Lovis', is_male=False, home='Mattisburg')
    
    mattis_rauberbande = RauberBande(mattis, 'Mattisburg', 'Mattisburg', name="Mattis' Räuberbande", people=[mattis, lovis])

    undis = Rauber(name='Undis', is_male=False, current_position='Mattiswald')
    borka = Rauber(name='Borka', is_male=True, current_position='Mattiswald')
    
    borkaräuber = RauberBande(borka, 'Mattisburg', 'Mattisburg', name="Borkaräuber", people=[undis, borka])
    
    # Start of Storry
    print('\n')
    print('Lightning strikes the Mattisburg and splits it in two.')
    ronja = lovis.give_birth(mattis, is_male=False, name='Ronja')
    birk = undis.give_birth(borka, True, 'Birk Borkason')
    print('\na few years later:')
    print('part of Festung now named "Borkafeste"')
    borkaräuber.set_new_home('Borkafeste')
    
    print(f'\nSome stuff happens to {ronja.name} and {birk.name} and thez help each other')
    ronja.add_friend(birk)
    
    print('\na little bit later:')
    ronja.move_to('Mattisburg')
    birk.move_to('Mattisburg')
    mattis.take_hostage(birk)
    mattis_rauberbande.start_conflict(borkaräuber)
    ronja.feels(f'Dosent like that {mattis_rauberbande.name} took {birk.name} as a hostage.')
    ronja.move_to('Borkafeste')
    borka.take_hostage(ronja)
    mattis.feels(f"Doesn't like that {ronja.name} is friends with {birk.name}")
    borka.feels(f"Doesn't like that {birk.name} is friends with {ronja.name}")
    
    mattis_rauberbande.stop_conflict(borkaräuber)
    mattis.release_hostage(birk)
    borka.release_hostage(ronja)
    
    ronja.move_to('verlassene Bärenhöhle')
    birk.move_to('verlassene Bärenhöhle')
    
    # print('\n')
    # for i in range(5):
    #     encounter.trigger_encounter()
    
    
    print('\nHalf a year later:')
    mattis.feels('is longing for his daughter')
    mattis.move_to('verlassene Bärenhöhle')
    mattis.talk('Pls come back.')
    mattis.move_to('Mattisburg')
    ronja.move_to('Mattisburg')
    birk.move_to('Borkafeste')
    
    print('\n')
    landsknechte.move_to('Mattiswald')
    landsknechte.ambush(mattis_rauberbande)
    landsknechte.ambush(borkaräuber)
    
    print('\n')
    vereinigten_tauberbande = mattis_rauberbande.merge_gruppe(borkaräuber, 'vereinigten Räuberbande', mattis)
    
    print('\nIn Spring:')
    # print(type(ronja))
    ronja = ronja.ich_will_kein_rauber_mehr_sein()
    # print(type(ronja))
    ronja.move_to('verlassene Bärenhöhle')
    birk.move_to('verlassene Bärenhöhle')
    
    # continue
    # verirren sich die drei Landsknechte Lars, Ludwig und Leroy im Wald. 
    lars.currently_with_group = False
    lars.move_to('Wald')
    ludwig.currently_with_group = False
    ludwig.move_to('Wald')
    leroy.currently_with_group = False
    leroy.move_to('Wald')
    
    
    
    
    

if __name__ == '__main__': main()