class Dog:
    def __init__(self, name, fur_color, race, age):
        self.name = name
        self.fur_color = fur_color
        self.race = race
        self.age = age

    def bark(self):
        return 'Woof!' * self.age

    def tail_wag(self, number):
        return f"{'mach' * self.age}".center(number, '~')


pixie = Dog("Pixie", "black & white", "border collie", 2)
print(pixie.name)
print(pixie.bark())
print(pixie.tail_wag(14))

dixie = Dog("Dixie", "yellow", "labrador", 5)
dust = Dog("Dust", "grey", "unknown", 4)
lassie = Dog("Lassie", "white", "lassie", 4)