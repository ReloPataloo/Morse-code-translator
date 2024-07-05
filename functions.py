MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def morse_to_text(code):
    text = ''
    character=''
    for letter in code:
        if (letter !='/'):
            i=0
            character +=letter
        else:
            i+=1
            if i==2:
                text=' '
            else:
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(character)]
                character = ''
    return text

def text_to_morse(code):
    morse = ''
    for letter in code:
        if letter != ' ':
            morse += MORSE_CODE_DICT[letter] + ' '
        else:
            morse += ' '
    return morse