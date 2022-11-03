from example_module import find_element, find_longest_word, NAMES_FR
from random import randint

names = ['Laura', 'Nickolas', 'Anna', 'Elizabeth', 'Patrick', 'Vicky']

max_len_name = find_longest_word(names)
id_anna = find_element("Anna", names)

print(max_len_name)
print(id_anna)
print(NAMES_FR)

print(randint(1, 200))