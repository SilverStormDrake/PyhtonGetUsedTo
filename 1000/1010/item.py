import csv

class Item:
    pay_rate = 0.8 #Discount example, 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Validating the Values
        assert price >= 0, f"Price {price} is invalid! Must be greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is invalid! Must be greater than 0"
        
        # Assing the Object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions To Execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def calculate_total_price(self):
        return self.price*self.quantity;

    def apply_pay_rate(self):
        self.price = self.price*self.pay_rate 
        # self : Instance Level 
        # <class_name> : Class Level

    # @classmethod # Used to import data from other format
    # def instantiate_from_csv(cls):
    #     with open('items.csv', 'r') as f:
    #         reader = csv.DictReader(f)
    #         items = list(reader)

    #     TODO: Find a way to fix this
    #     for item in items: 
    #          Item(
    #              name=item.get('name'),
    #              price=float(item.get('price')), 
    #              quantity=int(item.get('quantity')),
    #          )

    @staticmethod #Usado para referênciar os objetos instânciados, static methods do not need an paramether like self or cls
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}' , {self.price} , {self.quantity})"

