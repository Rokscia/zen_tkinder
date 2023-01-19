from constants import THIS_DATA


class FileWork:
    def __init__(self):
        self.file_name = 'output.txt'

    def write_to_file(self, text_to_enter: str = THIS_DATA, action: str = 'w'):
        with open(self.file_name, action) as text:
            text.write(text_to_enter)

    def read_from_file(self):
        try:
            with open(self.file_name, 'r') as text:
                return text.read()
        except FileNotFoundError:
            return 'File does not exist'

    def find_words_containing(self, symbols: str):
        if symbols == '':
            return 'You haven\'t entered anything'

        with open(self.file_name, 'r') as text:
            word_list = text.read().split()

        symbols_list = list(symbols.lower())
        words_found = ''
        for word in word_list:
            if all(i in word.lower() for i in symbols_list):
                words_found += f'{word} '

        if words_found == '':
            return 'No words found'
        return words_found

    def append_to_file(self, appendix: str):
        if appendix != '':
            self.write_to_file(f'{appendix}\n', 'a')

