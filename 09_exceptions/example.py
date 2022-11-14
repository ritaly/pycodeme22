# while True:
#     user_value = input("Podaj liczbę od 1 do 100")
#     if user_value.isnumeric():
#         user_value = int(user_value)
#         break

def get_calulation():
    try:
        num = int(input("Podaj cyfrę ->"))
        x = 5 / num
    except ZeroDivisionError:
        raise ValueError('LOL dzielisz przez zero')

    return x


def main():
    try:
        x = get_calulation()
    except ValueError as err: 
        print("Wystąpił błąd wartości, to nie jest prawidłowa wartość")
        print("-->>>", err)
    finally:
        print('FINANIE TUTAJ TRAFIE')

    print("Bye Bye!!!")
    print("Bye Bye!!!")
    print("Bye Bye!!!")
    print("Bye Bye!!!")
    # except ValueError:
    #     print("Wystąpił błąd")
    #     print("Ten string nie jest liczbą")

if __name__ == '__main__':
    main()
