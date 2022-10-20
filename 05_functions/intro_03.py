def sum_numbers(numbers_list):
    result_sum = 0
    for i in numbers_list:
        result_sum += i
    return result_sum


# --- main ---
num = [1, 2, 3, 4, 6, 4]
result = sum_numbers(num)
print(f"Suma z {num} to jest {result}")