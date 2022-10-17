my_tuple = (1, 2, 3, 4, 5, 12, 13, 14)

num = int(input("Give ma a number -> "))

# for index in range(len(my_tuple)):
#     if my_tuple[index] == num:
#         print("Index ->", index)

# for index, value in enumerate(my_tuple):
#     if value == num:
#         print("Index ->", index)

print(f"In number { num } in tuple -> { num in my_tuple }")
print(f"Number { num } is on index { my_tuple.index(num)}")