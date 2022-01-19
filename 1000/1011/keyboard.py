from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity: int,):
        #Super Function
        super().__init__(
            name, price, quantity
        )