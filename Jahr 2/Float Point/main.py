# Exercise:         Float Point Calc
# Created by:       Jonas Millonig
# Creation date:    19. 09. 2023


def convert_to_b(num: int, decimal_num: float = 0.0, max_lenght_decimal = 128) -> tuple[str, str]:     
    output_decimal = ''
    output_num = ''
    
    while num >= 1:
        output_num += str(int(num % 2))
        num = num / 2
    output_num = output_num[::-1]
    
    while decimal_num > 0 or len(output_decimal) <= max_lenght_decimal:
        decimal_num *= 2
        
        if int(decimal_num):
            output_decimal += '1'
            decimal_num -= 1
        else:
            output_decimal += '0'
    
    return output_num, output_decimal  
    
def shift(num: str, num_decimal: str):
    shift_amount = 0
    shift_right = int(num) == 0
    
    while int(num) != 1:
        if shift_right:
            shift_amount -= 1
            num += num_decimal[0]
            num_decimal = num_decimal[1:]
        else:
            shift_amount += 1
            num_decimal = num[-1] + num_decimal
            num = num[:-1]
    return num_decimal, shift_amount

def trim_num_b(num_b:str, bit_lenght:int, inverse_direction = False) -> str:
    to_manny = len(num_b) - bit_lenght
    
    if to_manny == 0:
        return num_b
    
    if len(num_b) > bit_lenght:
        if inverse_direction:
            #cut from right
            return num_b[:-to_manny]
        else:
            #cut from left
            return num_b[-to_manny:]
    else:
        output = ''
        while len(num_b) < bit_lenght:
            if inverse_direction:
                #fill right
                output += '0'
            else:
                #fill left
                output = '0' + output
        return output

def get_sign(num: float):
    sign = 0
    if num > 0: sign = 0
    else:
        num *= -1
        sign = 1
    return sign, num

# Code
def main():
    try:
        dezimal_input = float(input('Bitte gib eine zahl ein: '))
    except ValueError:
        print('Eingabe wert ungültig!')
        exit()
        
    sign, dezimal_input = get_sign(dezimal_input)
    num_d = [int(dezimal_input), dezimal_input % 1]
    num_b = convert_to_b(num_d[0], num_d[1])
    mantisse, shift_amount = shift(num_b[0], num_b[1])
    cut_mantisse = trim_num_b(mantisse, 23, True)
    exponent_char = trim_num_b(convert_to_b(shift_amount+127)[0], 8)
    
    print(f'{sign}|{exponent_char}|{cut_mantisse}')
    
if __name__ == '__main__': main()