def rectangle(x, y):
    print('x * y = ' + str(x * y))
    z.append(4) # zmienna z nie jest dostępna, to przypisanie NIE ZADZIAŁA

#--- main---
z = [3]
rectangle(3, 2)
print(z)