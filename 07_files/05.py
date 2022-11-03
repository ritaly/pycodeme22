def get_words():
    filename = 'text.txt'
    with open(filename, encoding="utf-8") as file:
        content = file.read().split()

    return content


def find_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word ):
            longest_word = word

    return longest_word


def main():
    word_list = get_words()
    print(find_longest_word(word_list))


main()