import random


def open_file():
    filename = input("Give me file name ...")
    with open(filename) as file:
        return file.readlines()


def get_random_quote(list_of_quotes):
    return random.choice(list_of_quotes).strip()


def show(quote):
    print("Quote of the day is:\n")
    txt, author = quote.split(' -')

    print('*' * 100)
    print(txt.center(100))
    print(author.center(100))
    print('*' * 100)


def main():
    quotes = open_file()
    quote = get_random_quote(quotes)

    show(quote)


main()