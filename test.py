import random

computer = random.randint(1, 101)
rounds = 6
last_distance = 200

while rounds > 0:
    rounds -= 1
    print(f"Rund do końca: {rounds}".center(30, "-"))

    while True:  # pętla do pobrania wartości od użytkonikwa
        user = input("Podaj liczbę od 1 do 100 ")  # czyli string zawiera liczbę
        if user.isnumeric():
            user = int(user)
            break  # wyjście z pętli
        else:
            print(f"Wpisano: {user} - to nie jest liczba!")
            print("Spróbuj jeszcze raz")
            continue

    if user == computer:
        print('Wygrywasz!')
        break

    else:
        current_distance = abs(computer - user)
        if current_distance < last_distance:
            print("cieplej!")
            last_distance = current_distance
        else:
            print("zimniej!")

    if rounds == 0 and user != computer:
        print("Przegrywasz!")
