import pandas as pd


def read_morse_data():
    morse_df = pd.read_csv('morse.csv')
    morse_df.caracter = morse_df['caracter'].astype(str).str.strip()
    morse_df.morse = morse_df['morse'].astype(str).str.strip()
    return morse_df


class TextToMorse:
    def __init__(self):
        self.morse_df = read_morse_data()

    def validate_text_before_convert(self, text_to_validate):
        for char in text_to_validate:
            if char.upper() not in self.morse_df['caracter'].values and char != ' ':
                return False
        return True

    def convert_text_to_morse(self, text_to_convert):

        morse_text = ''
        for char in text_to_convert:
            if char == ' ':
                morse_text += '/'
            else:
                indice_caracter = self.morse_df.index[self.morse_df['caracter'] == char.upper()]
                next_morse = self.morse_df.loc[indice_caracter, 'morse'].values[0]
                morse_text += next_morse + ' '
        return morse_text

    def validate_morse_before_decrypt(self, morse_to_validate):
        morse_list_words = [words for words in morse_to_validate.split('/')]
        morse_list_letters = [letter.split() for letter in morse_list_words]
        for word in morse_list_letters:
            for letter in word:
                if letter not in self.morse_df['morse'].values and letter != ' ':
                    return False
        return True

    def decrypt_morse(self, morse_text):
        morse_list_words = [words for words in morse_text.split('/')]
        morse_list_letters = [letter.split() for letter in morse_list_words]
        converted_morse = ''

        for word in morse_list_letters:
            for letter in word:
                index_morse = self.morse_df.index[self.morse_df['morse'] == letter]
                next_letter = self.morse_df.loc[index_morse, 'caracter'].values[0]
                converted_morse += next_letter
            converted_morse += ' '

        return converted_morse


