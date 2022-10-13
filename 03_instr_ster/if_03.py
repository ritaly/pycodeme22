grade1 = int('Oceń książkę od 1 - 10 -> ')
grade2 = int('Oceń książkę od 1 - 10 -> ')
grade3 = int('Oceń książkę od 1 - 10 -> ')

grades_avg = (grade1 + grade2 + grade3)/3

if grades_avg > 7:
    print("Bardzo dobra książka")
elif grades_avg >= 5:
    print("PRzeciętna")
else:
    print("Nie warta uwagi")