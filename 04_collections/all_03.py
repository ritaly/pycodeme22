n = int(input("Give number 1-10: "))

tab = [["-"] * n] * n

for row in tab:
    # print(' '.join(row))
    for col in row:
        print(col, end=" ")
    print()

