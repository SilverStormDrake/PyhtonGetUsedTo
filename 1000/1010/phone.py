from item import Item

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

