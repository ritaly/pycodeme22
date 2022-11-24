def square_area(side):
    return side * side


def rectagle_area(a, b):
    return a * b


def triagle_area(a,b):
    return a * b * 0.5


def main():
    result_s = square_area(5)
    print(result_s == 25)

    result_r = rectagle_area(5, 6)
    print(result_r == 30)
    print(result_r != 36)

if __name__ == '__main__':
    main()