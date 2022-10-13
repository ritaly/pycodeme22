grade1 = int(input('Oceń książkę od 1 - 10 -> '))
grade2 = int(input('Oceń książkę od 1 - 10 -> '))
grade3 = int(input('Oceń książkę od 1 - 10 -> '))

grades_avg = (grade1 + grade2 + grade3)/3

if grades_avg > 7:
    print("Bardzo dobra książka")
elif grades_avg >= 5:
    print("Przeciętna")
else:
    print("Nie warta uwagi")