
def sum_naturals_recursion(n):
    if n == 1:
        return 1
    return n + sum_naturals_recursion(n-1)

print(sum_naturals_recursion(10))