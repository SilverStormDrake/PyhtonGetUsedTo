#CSV - Comma separated values and Class Methods

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        #TODO: Find a way to fix this
        for item in items: 
            Item(
                name=item.get('name'),
                price=float(item.get('price')), 
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}' , {self.price} , {self.quantity})"




Item.instantiate_from_csv()
print(Item.all)