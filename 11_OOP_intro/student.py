class Student:
    university = "UAM"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def email(self):
        return f"{self.firstname}.{self.lastname}@{self.university}.com".lower()


student_A = Student("Anna", "Nowak", 23)
student_B = Student("Bartek", "Kowal", 24)

print("Mam na imię:", student_A.firstname + ' ' + student_A.lastname)
print(student_A.email())
print(student_B.email())

student_A.lastname = "Smith"
print("Mam na imię:", student_A.firstname + ' ' + student_A.lastname)


quote = "Zdrowie jest najwazniejsze"
print(type(quote))
print(quote.lower())
print(str.upper(quote))

print(student_A.email())
print(type(student_A))
print(Student.email(student_A))




