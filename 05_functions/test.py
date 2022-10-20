def add_book():
    title = input('Podaj tytuł książki')
    rate = int(input('Podaj ocenę tej książki'))
    list_books.append([title, rate])


def get_book():
    while True:
        numer = int(input("--> podaj numer ksiazki: "))
        if 3 >= numer >= 1:
            print("tytul: ", list_books[numer - 1][0], "ocena:", list_books[numer - 1][1])
            break
        else:
            print("numer nie istnieje")


# -- main ---

list_books = []
for i in range(3):
    print("Książka", i + 1)
    add_book()

print(list_books)

get_book()



