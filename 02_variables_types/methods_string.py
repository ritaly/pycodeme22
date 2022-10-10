# czy string zawiera conajmniej 1 dużą literę

txt = 'ABARACADABRA'

txt.isupper() #zawiera tylko duze liter

txt = 'abracaDAbra'

# 1. tekst jest tylko składający się z liter
# 2. nie zawiera tylko małych
print("Czy string jest tekstem zawierającym conajmniej 1 dużą literę ->", txt.isalpha() and not txt.islower())