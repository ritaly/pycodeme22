txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce ręce"""

txt = txt.lower()
txt = txt.replace(',', "")
txt = txt.split()

counting_dict = {}

for word in txt:
    if word not in counting_dict:
        counting_dict[word] = 1
    else:
        counting_dict[word] = counting_dict[word] + 1

for k, v in counting_dict.items():
    print(k, ":", v)


# uniq_word = set(txt)
#
# for word in uniq_word:
#     print(f"{word} -> {txt.count(word)}")