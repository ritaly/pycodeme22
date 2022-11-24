def check_values(*values):
    for item in values:
        if not isinstance(item, (int, float)):
            raise ValueError("Bok musi być wartością numeryczną!")


def square_area(a):
    check_values(a)

    return a * a


def rectangle_area(a, b):
    check_values(a, b)

    return a * b


def triangle_area(a, b):
    check_values(a, b)

    return a * b * 0.5


def trapezoid_area(a, b, h):
    check_values(a, b, h)

    return (a+b) * h * 0.5


def main():
    # result_s = square_area("lalala")
    # print(result_s == 25)

    result_r = rectangle_area(5, 'B')
    print(result_r)
    print(result_r != 36)


if __name__ == '__main__':
    main()