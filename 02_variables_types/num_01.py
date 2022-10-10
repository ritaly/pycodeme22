# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

spalanie_100 = 6.4
trasa = 120
cena = 5.04

result = cena * trasa/100 * spalanie_100

print('Cena całkowita trasy 120 km', round(result, 2), 'zł')