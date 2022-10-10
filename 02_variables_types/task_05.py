text = input("Give me a sentance to check palidrome -> ")
text = text.replace(" ", "")
text = text.lower()
print('Is palidrome? -> ', text == text[::-1])


