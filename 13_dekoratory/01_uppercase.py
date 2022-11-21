# dekorator upper case
def uppercase_decorator(func_param):
    def make_big():
        text = func_param()
        return text.upper()

    return make_big

# funkcja, która zwraca jakiś tekst



@uppercase_decorator
def show_string():
    return "Hakuna Matata"


print(show_string())