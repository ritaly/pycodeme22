from bmi import calculate_bmi, get_bmi_state


def open_file(filename):
    with open(filename) as file:
        return file.readlines()


def main():
    h = float(input('Height[m]:'))
    w = float(input("Weight[kg]: "))

    bmi = calculate_bmi(h, w)

    status = get_bmi_state(bmi)
    print(status)
    advice = open_file(status + '.txt')
    print(advice)


if __name__ == '__main__':
    main()