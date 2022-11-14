def sum_naturals_for(n):
    sum_number = 0

    for nr in range(1, n+1):
        sum_number = sum_number + nr

    return sum_number


def sum_naturals_while(n):
    sum_number = 0

    while n > 0:
        sum_number = sum_number + n
        n = n - 1

    return sum_number


print(sum_naturals_for(10))
print(sum_naturals_while(10))
