def get_safe_value(message):
    while True:
        try:
            value = float(input(message))
            break
        except ValueError as err:
            print('Try again, error:', err)

    return value


def get_possible_value(msg, v_min, v_max):
    while True:
        value = get_safe_value(msg)
        if value < v_min or value > v_max :
            print("This is impossible value")
        else:
            break
    return value


def get_user_params():
    h = get_possible_value('Height[m]:', 1.3, 2.3)
    w = get_possible_value('Weight[kg]:', 20, 200)

    return h, w


def calculate_bmi(h, w):
    bmi = w / (h ** 2)
    print('BMI result:', round(bmi, 2))
    return bmi


def get_bmi_state(bmi):
    if bmi < 18:
        return 'underweight'
    elif bmi <= 25:
        return 'standard'
    elif bmi <= 30:
        return 'overweight'
    else:
        return 'obesity'


def main():
    get_user_params()
    # result_bmi = calculate_bmi(*get_user_params())
    # status = get_bmi_state(result_bmi)
    # print(status)


if __name__ == '__main__':
    main()
