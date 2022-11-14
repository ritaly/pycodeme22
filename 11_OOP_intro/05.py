class Shop:
    def __init__(self, items: list) -> None:
        self.items = items

    def show_product(self, item_id):
        try:
            product, size = self.items[item_id]
            print(f"{product} - rozmiar {size}")
        except (IndexError, TypeError):
            print('Nie ma produktu o takim id')

    def try_product(self, item_id, user_size):
        try:
            product, size = self.items[item_id]
            if size == user_size:
                print("Rozmiar pasuje")
            else:
                print("To nie ten rozmiar")
        except (IndexError, TypeError):
            print("Nie ma produktu o takim id")

    def buy_product(self, item_id):
        try:
            print(f"Kupujesz {self.items[item_id]}")
            self.items.pop(item_id)
        except (IndexError, TypeError):
            print("Nie ma takiego produktu")

    def return_product(self, product):
        if len(product) == 2:
            self.items.append(product)
            print("Dokonano zwrotu")
        else:
            print("To nie jest produkt u nas kupiony")


def main():
    fashionshop = Shop([
        ["tshirt", "S"],
        ["dress", "L"],
        ["shorts", "M"]
    ])

    fashionshop.show_product(2)
    fashionshop.try_product(2, 'XL')
    fashionshop.buy_product(2)
    print(fashionshop.items)
    fashionshop.return_product(["trouser", "XL"])
    print(fashionshop.items)


if __name__ == '__main__':
    main()
