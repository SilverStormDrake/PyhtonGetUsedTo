#Inheritance

import csv

class Item:
    pay_rate = 0.8 #Discount example, 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Validating the Values
        assert price >= 0, f"Price {price} is invalid! Must be greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is invalid! Must be greater than 0"
        
        # Assing the Object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions To Execute
        Item.all.append(self)

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


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        #Super Function
        super().__init__(
            name, price, quantity
        )
        
        # Validating the Values
        assert broken_phones >= 0, f"Broken_phones {broken_phones} is invalid! Must be greater than 0"


        # Assing the Object

        self.broken_phones = broken_phones
    

phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Phone("jscPhonev20", 700, 5, 1)
print(Item.all)
print(Phone.all)