import random

MOVES = ("k", "p", "n")

winner_looser = {
    "k": "n",
    "n": "p",
    "p": "k"
}


def get_user_choice():
    message = """ Wybierz ruch
    * k - kamień
    * p - papier
    * n - nożyce
    * koniec - aby zakończyć grę

    --> """

    choice = input(message)
    return choice


def add_result(user_choice, computer_choice, results):
    if user_choice == computer_choice:
        print("Remis")
        results["remis"] += 1

    elif winner_looser[user_choice] == computer_choice:
        print("Użytkownik wygrywa")
        results["uzytkownik"] += 1
    else:
        print("Komputer wygrywa")
        results["komputer"] += 1


def show_result(results_dict):
    print()
    print("Tablica wyników".center(30, "-"))

    for k, v in results_dict.items():
        print(k, ' -> ', v)


results = {
    "komputer": 0,
    "uzytkownik": 0,
    "remis": 0
}

rounds = int(input("Ile rund chcesz zagrać? 1-10"))

for nr in range(rounds):
    print(f"Runda {nr + 1}".center(30, "-"))

    user = get_user_choice()

    if user == 'koniec':  # sprawdzenie warunku końca
        print('Wybrano koniec gry!')
        break

    computer = random.choice(MOVES)

    print(f"Komputer wybrał {computer}, użytkownik wybrał {user}")

    # wywołać sprawdzenie punktów/wyniku
    add_result(user, computer, results)

show_result(results)