import os
import beaupy
import codecs
from pystyle import Colors, Colorate




##--------------------------Functions------------------------------##

def banner():
    banner = """
                ▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄▄▄ .▄▄▄
                ▀▄ █·▪     •██  •██  ▀▄.▀·▀▄ █·
                ▐▀▀▄  ▄█▀▄  ▐█.▪ ▐█.▪▐▀▀▪▄▐▀▀▄
                ▐█•█▌▐█▌.▐▌ ▐█▌· ▐█▌·▐█▄▄▌▐█•█▌
                .▀  ▀ ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀

          Made by 0x4b | https://github.com/0xNibble
    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return colored_banner




def clear():
    os.system("clear||cls")



#Rot47 Encode & Decode
def r47e(message: str) -> str:
    encoded_message = ""
    for char in message:
        char_code = ord(char)
        if char_code >= 33 and char_code <= 126:
            char_code -= 47
            if char_code < 33:
                char_code += 94
        encoded_message += chr(char_code)
    return encoded_message


def r47d(message: str) -> str:
    decoded_message = ""
    for char in message:
        char_code = ord(char)
        if char_code >= 33 and char_code <= 126:
            char_code += 47
            if char_code > 126:
                char_code -= 94
        decoded_message += chr(char_code)
    return decoded_message



#Rot13 Encode & Decode
def r13e(message: str) -> str:
    return codecs.encode(message, "rot13")

def r13d(message: str) -> str:
    return codecs.decode(message, "rot13")

##--------------------------Functions End---------------------------------##







##--------------------------Main Code---------------------------------##

def main():
    options = ['Rot13', 'Rot47',  'Exit?']
    while True:
        clear()
        print(f'{banner()}\n\nWhat would you like to do? - (Main Menu)\n-----------------------------------------------------------\n')
        option = beaupy.select(options, cursor_style="#ffa533")

        if not option:
            clear()
            exit("Keyboard Interuption Detected!\nGoodbye!")


        if options[0] in option:
            while True:
                clear()
                rot13_options = ['Encode?', 'Decode', 'Back?']
                print(f'{banner()}\n\nWhat would you like to do? - (Rot13)\n-----------------------------------------------------------\n')
                rot13_option = beaupy.select(rot13_options, cursor_style="#ffa533")

                if not rot13_option:
                    clear()
                    break

                if rot13_options[0] in rot13_option:
                    clear()
                    m13e = beaupy.prompt("What would you like to encode?")
                    if not m13e or m13e == '':
                        clear()
                        break

                    data13e = r13e(m13e)
                    clear()
                    print(f"Here is your encodded message: {data13e}\n\n")
                    input('Press "enter" to continue...')


                if rot13_options[1] in rot13_option:
                    clear()
                    m13d = beaupy.prompt("What would you like to decode?")
                    if not m13d or m13d == '':
                        clear()
                        break
                    data13d = r13d(m13d)
                    clear()
                    print(f"Here is your decodded message: {data13d}\n\n")
                    input('Press "enter" to continue...')

                if rot13_options[2] in rot13_option:
                    clear()
                    break


        if options[1] in option:
            while True:
                clear()
                rot47_options = ['Encode?', 'Decode', 'Back?']
                print(f'{banner()}\n\nWhat would you like to do? - (Rot47)\n-----------------------------------------------------------\n')
                rot47_option = beaupy.select(rot47_options, cursor_style="#ffa533")

                if not rot47_option:
                    clear()
                    break

                if rot47_options[0] in rot47_option:
                    clear()
                    m47e = beaupy.prompt("What would you like to encode?")
                    if not m47e or m47e == '':
                        clear()
                        break
                    data47e = r47e(m47e)
                    print(f'Here is your encodded message: {data47e}\n\n')
                    input('Press "enter" to continue...')


                if rot47_options[1] in rot47_option:
                    clear()
                    m47d = beaupy.prompt("What would you like to decode?")
                    if not m47e or m47e == '':
                        clear()
                        break
                    data47d = r47d(m47d)
                    print(f'Here is your decodded message: {data47d}\n\n')
                    input('Press "enter" to continue...')

                if rot47_options[2] in rot47_option:
                    clear()
                    break


        if options[2] in option:
            clear()
            exit("Goodbye")

##--------------------------Main Code End---------------------------------##





if __name__ == '__main__':
    clear()
    main()
