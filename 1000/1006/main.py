#Access to all objects of a class

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

    def __repr__(self):
        return f"Item('{self.name}' , {self.price} , {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

