def readfile_to_list(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read().splitlines()


def give_word(words_list):
    return words_list[0]


def get_filtered_words(words_list, letter, position: int, action):
    words_list_temp = []
    for w in words_list:
        if (action == "matches" and w[position] == letter) or \
                (action == "absent" and letter not in w) or \
                (action == "exists" and w[position] != letter and letter in w):
            words_list_temp.append(w)
    return words_list_temp


if __name__ == "__main__":

    first_words = readfile_to_list("words_count_sorted.txt")
    all_words = readfile_to_list("5letters.txt")
    for _ in range(6):
        letters_exist = ()
        if len(first_words) > 0:
            word = give_word(first_words)
            first_words.remove(word)
        else:
            word = give_word(all_words)
            all_words.remove(word)
        print(word)
        choices = {"1": "matches", "2": "absent", "3": "exists"}
        for i in range(5):
            choice = input(
                f"Does {i + 1} letter ({word[i]}) matches? 1 - matches to the place, 2 - does not exist, 3 - another "
                f"place\n")
            first_words = get_filtered_words(first_words, word[i], i, choices[choice])
            all_words = get_filtered_words(all_words, word[i], i, choices[choice])
