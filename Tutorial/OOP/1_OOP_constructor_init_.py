class Item:
    pay_rate = 0.8 # The pay rate after 20% discount # Class attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance created: {name}")

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'


item1 = Item('Phone', 100, 5)
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
print('item1.calculate_total_price = ', item1.calculate_total_price())
# print(item1.name, item1.price, item1.quantity)

item2 = Item('Laptop', 1000, 3)
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 3
print('item2.calculate_total_price = ', item2.calculate_total_price())
# print(item2.name, item2.price, item2.quantity)


print('Item.pay_rate = ', Item.pay_rate)
print('item1.pay_rate = ', item1.pay_rate)
print('item2.pay_rate = ', item2.pay_rate)

print('Class Item attributes = ', Item.__dict__)  # All attributes for Class level
print('instance item1 attributes = ', item1.__dict__)  # All attributes for instance level


item1.apply_discount()
print('item1.price + 20% discount = ', item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print('item2.price + 30% discount = ', item2.price)


item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

print('Item.all = ', Item.all)

for instance in Item.all:
    print('instance.name = ', instance.name)
