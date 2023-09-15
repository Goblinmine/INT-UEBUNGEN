# Exercise:         Mail merge
# Created by:       Jonas Millonig
# Creation date:    15. 09. 2023

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
   
def get_people(invited_names_file: str) -> list[str]:
    with open(invited_names_file) as file:
        people = [line.removesuffix('\n') for line in file.readlines()]
        return people

def get_starting_letter(starting_letter_file: str) -> str:
    with open(starting_letter_file) as inputfile:
        return inputfile.read()

def make_letters(people: list[str], starting_letter: str, output_path: str) -> None:
    for person in people:
            with open(f'{output_path}/{person}.txt','w') as outputfile:
                outputfile.write(starting_letter.replace('[name]',person)) 
    

def main(workingdir: str, invited_names_file: str, starting_letter_file: str, output_path: str) -> None:
    people = get_people(workingdir + invited_names_file)
    starting_letter = get_starting_letter(workingdir + starting_letter_file)
    make_letters(people, starting_letter, workingdir + output_path)    

if __name__ == '__main__': main('Jahr 2/MailMerge/', 'Input/Names/invited_names.txt','Input/Letters/starting_letter.txt', 'Output/ReadyToSend')