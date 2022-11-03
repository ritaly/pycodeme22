from calendar import show_month


list_elem = [
    ['happy', range(20)],
    ['sad', range(30)],
    ['angry', range(10)],
]

data = dict(list_elem)

for name, days_range in data.items():
    show_month(name, days_range)