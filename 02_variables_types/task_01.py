txt = 'abrakadabra'
length = len(txt)

index_center = length // 2
index_prev = index_center - 1
index_next = index_center + 1

print(txt[index_prev] + txt[index_center] + txt[index_next])

print(txt[index_prev:index_next+1])

