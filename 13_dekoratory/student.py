import datetime

class Student:
  min_avg = 4.5
  university = 'New York Academy'

  def __init__(self, name, last, age, student_avg):
    self.name = name
    self.last = last
    self.age = age
    self.student_avg = student_avg

  def __str__(self):
    return self.name.capitalize() + " " + self.last.capitalize()

  def email(self):
    return '{}.{}.university.com'.format(self.name, self.last)

  def grant_scholarship(self):
    if self.student_avg > self.min_avg:
      print('Przyznano stypendium')
    else:
      print('Odmowa przyznania stypendium')

  @classmethod
  def set_min_avg(cls, average):
    cls.min_avg = average

  @staticmethod
  def is_academic(day):
    if day.weekday() == 5 or day.weekday() == 6: #sobota / niedziela
      return False
    else:
      return True



obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 4.6)

Student.set_min_avg(4.6)

print(obj_anna.min_avg)
print(Student.min_avg)
print(obj_arek.min_avg)
obj_arek.grant_scholarship()
obj_anna.grant_scholarship()


today = datetime.date.today()
print(today)

print("Do we have lessons today?")
print(Student.is_academic())