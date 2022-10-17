letters = ('a', 'b', 'a', 'c', 'a', 'b', 'g')
numbers = (1, 2, 3, 1, 1, 3, 2, 2, 3, 4)

print(letters[::2])
print(numbers[1::2])

new_list = list(letters[::2] + numbers[1::2])
print(new_list)

print(set(new_list))