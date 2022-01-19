from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("MyItem", 750, 6)
item2 = Phone("NewPhone", 1000, 3, 0)
item3 = Keyboard("LG", 200, 3)

item2.apply_increment(0.2)
item3.apply_discount()

print(item3.price)
