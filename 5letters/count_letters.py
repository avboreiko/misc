
def readfile_to_list(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read().splitlines()


class WordsDict:
    def __init__(self, words_file):
        self.words = readfile_to_list(words_file)
        self.words_file = words_file
        self.non_repeated_letters_words = None
        self.filter_repeated_letters_words()

    def filter_repeated_letters_words(self):
        non_repeated_letters_words = []
        for word in self.words:
            for i in range(len(word)):
                if i != word.rfind(word[i]):
                    break
            else:
                non_repeated_letters_words.append(word)
        self.non_repeated_letters_words = non_repeated_letters_words


def count_words_value(words: list, letters_count: dict):
    words_values = dict()
    for word in words:
        word_value = 0
        for i in word:
            word_value += letters_count[i]
        words_values[word] = word_value
    return words_values


def sort_words_by_values(words_values: dict):
    return dict(sorted(words_values.items(), key=lambda item: item[1], reverse=True))


def prepare_dict():
    letters_dict = {i.lower(): 0 for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-"}
    return letters_dict


def count_letters(words: list, letters_dict: dict):
    for word in words:
        for letter in letters_dict.keys():
            if letter in word:
                letters_dict[letter] += 1
    return letters_dict


def write_dict_to_file(dict_to_write, filename):
    with open(filename, 'w', encoding="utf-8") as output:
        for key in dict_to_write.keys():
            output.write(f"{str(key)}\n")


def sort_letters_ammount(letters_dict):
    return dict(sorted(letters_dict.items(), key=lambda item: item[1], reverse=True))


if __name__ == "__main__":
    wordsDict = WordsDict("5letters.txt")
    alphabet_dict = prepare_dict()
    alphabet_count = count_letters(wordsDict.words, alphabet_dict)
    alphabet_count = sort_letters_ammount(alphabet_count)
    write_dict_to_file(alphabet_count, "result.txt")

    words_count = count_words_value(wordsDict.non_repeated_letters_words, alphabet_count)
    words_count_sorted = sort_words_by_values(words_count)
    write_dict_to_file(words_count_sorted, "words_count_sorted.txt")



# How to find a word with the most popular letters:
# 1. the word should not contain repeated symbols - find all words with unique letters
# 2. value each word by its letters places - go through a word and count each letter place, sum all
# 3. take the max valued word

