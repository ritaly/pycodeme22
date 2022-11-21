from random import choice

def stars_decorator(func_param):
    def nested():
        quote = func_param()
        stars = 60 * '*'

        txt = stars + '\n' + quote.center(60) + '\n' + stars
        return txt

    return nested


@stars_decorator
def get_quote():
    quotes = [
        "Be or not to be",
        "Life is a long lesson in humility.",
        "Whatever you are, be a good one",
        "Be yourself; everyone else is already taken.",
        "Happiness depends upon ourselves.",
    ]
    return choice(quotes)


def main():
    print(get_quote())


if __name__ == "__main__":
    main()