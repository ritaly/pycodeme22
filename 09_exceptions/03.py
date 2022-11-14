items = [1, 0, "string", 22.3, "lista", 6, 7, 8, 9, (), {'key': 'klucz'}, True]

try:
    index = int(input('Podaj index ->'))
    result = 1 / items[index]
except ValueError:
    print("Błędna wartość")
except ZeroDivisionError:
    print("Nie dziel przez zero!")
except TypeError:
    print("Błąd typu")
except IndexError:
    print("Wyszliśmy poza zakres tablicy. WRAAACAAAJ")
