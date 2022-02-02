class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


# d = Dog("Tim", 12)
# d.set_age(10)
# print(d.get_age())
# d_2 = Dog('Bill', 3)
# print(d_2.get_age())
# #d.bark()
# #print(d.add_one(5))
# print(type(d))


