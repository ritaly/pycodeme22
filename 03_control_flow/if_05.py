# Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę,
# 1 dużą literę
# mieć długość conajmniej 8 znaków, a nie dłuższe niż 24

password = input('Podaj testowe hasło -> ')

if len(password) < 8 or len(password) > 24:
    print("długość hasła nieprawidłowa, oczekiwana długosć między 8 a 24 znaki")
if password.isdigit():
    print("hasło powinno zawierać też litery")
if password.isalpha():
    print("hasło powinno zawierać też cyfry")
if password.islower():
    print("hasło zawiera tylko małe litery, a powinno zawierać conajmniej 1 dużą literę")
if password.isupper():
    print("hasło zawiera tylko duże litery, a powinno zawierać conajmniej 1 małą literę")
