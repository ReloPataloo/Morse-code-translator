from functions import morse_to_text, text_to_morse

while True:
    print("""Select mode:
1. Morse to Text (under the form "...././.-../.-../")
2. Text to Morse in upper letters only""")
    
    mode = input()
    if mode == "1":
        print("Enter your code: ")
        code=str(input())
        print(morse_to_text(code))
        break
    elif mode == "2":
        print("Enter your code: ")
        code=str(input())
        print(text_to_morse(code))
        break
    else:
        print("Invalid input. Please try again.")