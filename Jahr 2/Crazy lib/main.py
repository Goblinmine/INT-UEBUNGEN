# Exercise:         Crazy lib
# Created by:       Jonas Millonig
# Creation date:    12. 09. 2023

placeholder = {'VERB_ING', 'NOUN', 'ADJECTIVE'}

def makeCrazyLib(filename: str) -> str:
    text = ''
    try:
        with open(filename) as file:
            for line in file:
                text += processLine(line)
    except FileNotFoundError:
        print(f'File "{filename}" nicht gefunden!')
    finally:
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

def save_crazy_lib(filename: str, text: str) -> None:
    try:
        with open(filename, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print(f'File "{filename}" nicht gefunden!')
    pass


def main() -> None:
    filename = 'Jahr 2/Crazy lib/lib.txt'
    text = makeCrazyLib(filename)
    print(text)
    save_crazy_lib(filename, text)

if __name__ == '__main__': main()