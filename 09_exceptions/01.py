items = [13, "string", 2.45, 0, {}, True, False, []]

for i in items:
    try:
        x = 10 / i
        print(x)
    except TypeError:
        print("type error for", i)
    except ZeroDivisionError:
        print("zero div error", i)