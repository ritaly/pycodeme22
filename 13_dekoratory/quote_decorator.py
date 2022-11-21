from random import choice


# Napisz dekorator addstars zmieniający sposób wyświetlania cytatu
# na taki:
#
# *********************************
#             cytat
# *********************************
def stars_decorator(function):
    def nested():
        quote = function()
        # ...

    return nested

@stars_decorator
def get_quote():
    quotes = [
        "Be or not to be",
        "Life is a long lesson in humility.",
        "Whatever you are, be a good one",
        "Be yourself; everyone else is already taken.",
        "Happiness depends upon ourselves."
    ]
    return choice(quotes)


def main():
    print(get_quote())


if __name__ == "__main__":
    main()
