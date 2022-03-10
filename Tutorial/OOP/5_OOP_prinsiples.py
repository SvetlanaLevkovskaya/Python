"""
1 - Encapsulation
2 - Abstraction
3 - Inheritance
4 - Polymorphism
"""
"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
# 1 - Encapsulation
# 2 - Abstraction

from item import Item

item1 = Item("MyItem", 750, 6)

item1.apply_increment(0.2)
item1.apply_discount()
print('MyItem price = ', item1.price)

item1.send_email()

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
# 3 - Inheritance
from phone import Phone

item1 = Phone("jscPhone", 1000, 3)
item1.apply_increment(0.2)
item1.apply_discount()
print('jscPhone = ', item1.price)

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
# 4 - Polymorphism
name = "Jim"   #str
print(len(name))

some_list = ["some", "name"] # list
print(len(some_list))
# That's polymorphism in action, a single function does know
# how to handle different kinds of objects as expected!

from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount()
print('jscKeyboard = ', item1.price)

print("Python".zfill(6))

