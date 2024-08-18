class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def __is_true(self, char):
        return True if (char.isalpha() or char == '\'' or char == ' ') else False

    def __filter_str(self, str):
        str = str.lower()
        # str = filter(self.__is_true, str)
        return ''.join(list(filter(self.__is_true, str)))

    def get_all_words(self):

        for file in self.file_names:
            all_words = {}
            list = []
            try:
                with open(file, encoding='UTF-8') as f:
                    while True:
                        str = f.readline()
                        if str == '':
                            break
                        else:
                            for x in self.__filter_str(str).split():
                                list.append(x)
                    all_words[file] = list
                    return all_words
            except IOError:
                print(f'Не удальсь открыть файл {file}')

    def find(self, word):
        find_word = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            for i in range(len(value)):
                if value[i] == word.lower():
                    find_word[key] = i + 1
                    break
        return find_word

    def count(self, word):
        count_word = {}
        count = 0
        all_words = self.get_all_words()
        for key, value in all_words.items():
            count = value.count(word.lower())
            if count:
                count_word[key] = count

        return count_word


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

