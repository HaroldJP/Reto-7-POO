class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Beverage(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class FastFood(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Lunch(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Protein(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.kind = kind

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items)
        return total_price

    def __iter__(self):
        return OrderIterator(self.items)

class OrderIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

if __name__ == "__main__":

    coca_cola = Beverage(name="Coca-cola", price=3500, kind="Cold beverage")
    orange_juice = Beverage(name="Orange juice", price=3000, kind="Cold beverage")
    lemonade = Beverage(name="Lemonade", price=2500, kind="Cold beverage")
    water = Beverage(name="Water", price=2000, kind="Cold beverage")
    coffee = Beverage(name="Coffee", price=2500, kind="Hot beverage")
    chocolate = Beverage(name="Chocolate", price=2500, kind="Hot beverage")

    hot_dog = FastFood(name="Hot dog", price=10000, kind="Big sausage")
    hamburguer = FastFood(name="Hamburguer", price=12000, kind="Double beef")
    pizza = FastFood(name="Pizza", price=8000, kind="Extra cheese")

    lentils = Lunch(name="Lentils with rice and salad", price=7000, kind="Ordinary")
    beans = Lunch(name="Beans with rice and salad", price=7000, kind="Ordinary")
    pasta = Lunch(name="Pasta with bread and salad", price=6500, kind="Executive")

    beef = Protein(name="Beef", price=6000, kind="Cow")
    chicken = Protein(name="Chicken", price=5500, kind="Chicken meal")
    fish = Protein(name="Mojarra", price=7800, kind="Fish meal")

    # Enter your order
    your_order = [water, lentils, chicken, pizza]

    order = Order(your_order)

    # Total price
    total_price = order.calculate_total_price()

    print("Order:")
    for item in order:
        print(f"- {item.name}: ${item.price}")

    print(f"Total price: ${total_price}")
