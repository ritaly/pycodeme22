import os
import sys

print(sys.path)

filename = 'pantadeusz.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('Nie ma takiego pliku')