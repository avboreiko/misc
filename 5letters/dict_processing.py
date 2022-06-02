

def word_length(word: str, length: int) -> bool:
    if word.__len__() == length:
        return True


def filter_file(filename: str, output_file_name: str):
    with open(filename, 'r', encoding="utf-8") as file:
        with open(output_file_name, 'w', encoding="utf-8") as output:
            for line in file.readlines():
                if word_length(line, 6):
                    output.writelines(line)


if __name__ == "__main__":
    filter_file('singular.txt', '5letters.txt')
