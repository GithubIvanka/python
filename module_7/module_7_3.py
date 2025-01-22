import re


class WordsFinder:

    def __init__(self, *args: str):
        self.file_names = args

    def get_all_words(self) -> dict:
        all_words = {}

        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as open_file:
                text = open_file.read()
                text = re.sub(r"[^a-zA-Z0-9а-яА-Я\s]", "", text)
                all_words[open_file.name] = list(str.split(text))
        return all_words

    def find(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            count = 0
            for text in words:
                count += 1
                if str(text).lower() == str(word).lower():
                    find_words[name] = count
                    break
        return find_words

    def count(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            num = 0
            for text in words:
                if str(text).lower() == str(word).lower():
                    num += 1
            find_words[name] = num
        return find_words


if __name__ == "__main__":
    finder2 = WordsFinder("test_file.txt")

    print(finder2.get_all_words())  # Все слова
    print(finder2.find("TEXT"))  # 3 слово по счёту
    print(finder2.count("teXT"))  # 4 слова teXT в тексте всего
