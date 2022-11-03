print("Jestem w example_module!")

NAMES_FR = ("Charles", "Geal", "Pierre")

def find_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def find_element(target, sequence):
    """Finds element in a sequence"""
    for index, value in enumerate(sequence):
        if value == target:
            return index

    return -1


def get_words():
    filename = 'text.txt'
    with open(filename, encoding="utf-8") as file:
        content = file.read().split()

    return content