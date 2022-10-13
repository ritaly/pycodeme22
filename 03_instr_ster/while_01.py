# w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

# fahr = 0
while fahr <= 200:
    celc = 5 / 9 * (fahr - 32)
    celc = round(celc, 2)
    print(f"{fahr} st Fahrenheit'a  → {celc} st C")
    fahr += 20


for fahre in range(0, 201, 20):
    celc = 5 / 9 * (fahre - 32)
    celc = round(celc, 2)
    print(f"{fahre} st Fahrenheit'a  → {celc} st C")