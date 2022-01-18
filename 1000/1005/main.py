#class atributes

class Item:
    pay_rate = 0.8 #Discount example, 20% discount
    def __init__(self, name: str, price: float, quantity: int):
        #Validating the Values
        assert price >= 0, f"Price {price} is invalid! Must be greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is invalid! Must be greater than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity;

    def apply_pay_rate(self):
        self.price = self.price*self.pay_rate 
        # self : Instance Level 
        # <class_name> : Class Level


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item1.apply_pay_rate()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_pay_rate()
print(item2.price)



