# Exercise:         Crazy lib
# Created by:       Jonas Millonig
# Creation date:    12. 09. 2023

placeholder = {'VERB_ING', 'NOUN', 'ADJECTIVE'}

def makeCrazyLib(filename: str) -> str:
    text = '\n'
    with open(filename) as file:
        for line in file:
            text += processLine(line)
    return text

def processLine(line: str) -> str:
    processdLine = ''
    for word in line.split():
        stripped = word.strip('.,;?!')
        if stripped in placeholder:
            wordToReplace = input(f'Replace {stripped} with: ')
            if word[-1] in '.,;?!':
                wordToReplace += word[-1]
            processdLine += f'{wordToReplace} '
        else:
            processdLine += f'{word} '
    processdLine += '\n' 
    return processdLine


def main() -> None:
    print(makeCrazyLib('Jahr 2/Crazy lib/lib.txt'))

if __name__ == '__main__': main()