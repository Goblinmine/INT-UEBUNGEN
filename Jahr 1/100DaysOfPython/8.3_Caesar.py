# Exercise:         Day 8.3 | Caesar Verschlüsselung
# Created by:       Jonas Millonig
# Creation date:    13.03.2023

# a-z -> 97-122

def main():
    while True:
        mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        output = ""

        if mode == 'encode':
            for letter in message:
                letterCode = ord(letter)
                if letterCode > (122 - shift):
                    output += chr(letterCode + shift - 26)
                else:
                    output += chr(letterCode + shift)    
            print(f"Here's the encoded result: {output}")
            
            
        elif mode == 'decode':
            for letter in message:
                letterCode = ord(letter)
                
                if letterCode < (97 + shift):
                    output += chr(letterCode - shift + 26)
                else:
                    output += chr(letterCode - shift) 

            print(f"Here's the decoded result: {output}")
           
        else:
            raise ValueError("Input not valid!")

        if input("Type 'yes' if you want to go again. Otherwise type 'no'.") != 'yes':
            break
        
main()