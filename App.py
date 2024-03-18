from Converter import TextToMorse

converter = TextToMorse()
OPTION_CONVERT_TEXT = 1
OPTION_DECRYPT_MORSE = 2
OPTION_EXIT = 3

while True:
    option = int(input("\n1- Convert a text to morse\n2- Exit the program\nEnter your option: "))

    if option == OPTION_CONVERT_TEXT:

        text = input("\nRemember the spaces will be represented as '/' and the morse code does not "
                     "accept special caracters\n"
                     "Enter the text to convert to morse code:")
        validation_text = converter.validate_text_before_convert(text_to_validate=text)

        while not validation_text:
            text = input("\nYour text has unnusual characters!\n Please re-write your text with only "
                        "alphanumeric characters!!"
                         "\nEnter the text again: ")
            validation_text = converter.validate_text_before_convert(text_to_validate=text)

        converted_text = converter.convert_text_to_morse(text_to_convert=text)
        print(f'The converted text to morse is:\n{converted_text}')

    elif option == OPTION_DECRYPT_MORSE:
        morse = input("\nRemember the spaces between the words in morse are represented as '/' dont forget them!\n"
                      "Enter the morse code to be decrypted:")
        validation_morse = converter.validate_morse_before_decrypt(morse_to_validate=morse)

        while not validation_morse:
            morse = input("Your morse code has wrong codes or is not separated by the '/' between the words!!"
                          "Dont forget them!"
                          "\nEnter the code again: ")
            validation_morse = converter.validate_morse_before_decrypt(morse_to_validate=morse)

        converted_morse = converter.decrypt_morse(morse_text=morse)
        print(f'The morse converted to text is  {converted_morse}')

    elif option == OPTION_EXIT:
        print("Thanks for using, exiting the program...")
        break

    else:
        print("Invalid option! Please try a valid one!")
