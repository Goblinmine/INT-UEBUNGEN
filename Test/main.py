
vocal_chars: set[str] = None

def init_vocal_chars():
    global vocal_chars
    vocal_chars = {'a', 'ä', 'e', 'i', 'o', 'ö', 'u', 'ü'}
    vocal_chars_upper = [char.upper() for char in vocal_chars]
    vocal_chars.update(vocal_chars_upper)

def read_file(file_path: str) -> str:
    with open(file_path, encoding='UTF-8') as file:
        return file.read()

def geheimsprache(input_text: str) -> str:
    if vocal_chars == None:
        init_vocal_chars()
        
    if input_text.strip() == '': raise ValueError('Input is empty str.')
    
    output_text = ''
    for char in input_text:
        if char in vocal_chars:
            output_text += f'{char}b{char}'
        else:
            output_text += char
    return output_text
        
def save_geheimsprache(text: str, mode = 'override'):
    file_path = 'Geheimcode.txt'
    # modes = {'append', 'override'}
    # if mode not in modes:
    #     raise ValueError(f'{mode} not a valid mode! \nOnly "append" and "override" are valid modes.')
    
    match mode:
        case 'append':
            mode = 'a'
        case 'override':
            mode = 'w'
        case _:
            raise ValueError(f'{mode} not a valid mode! \nOnly "append" and "override" are valid modes.')
    
    with open(file_path, mode) as file:
        file.write(text)

def main(file_path: str):
    try:
        output_text = read_file(file_path)
        output_text = geheimsprache(output_text)
        save_geheimsprache(output_text, mode='test')
        print(output_text)
    # i decided to catch all exeption here in the main file instead of in each function
    # bc. because the program should not continue if there is an error.
    except FileNotFoundError as error:
        print(f'ERROR: "{error.filename}" not found')
    except IsADirectoryError as error:
        print(f'ERROR: {error.strerror} for "{error.filename}" file')
    except PermissionError as error:
        print(f'ERROR: {error.strerror} for "{error.filename}" file')
    except ValueError as error:
        print(f'ERROR: {error}')

main(file_path='Sources/einText.txt')