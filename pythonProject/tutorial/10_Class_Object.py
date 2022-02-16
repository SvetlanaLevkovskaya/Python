class House:
    """description"""
    def __init__(self, street, number):
        """house's property"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """ build a house"""
        print("House on the street " + self.street + "has a number " + str(self.number))

    def age_of_house(self, year):
        self.age += year

# House_1 = House("First", 20)
# House_2 = House("Second", 22)
#
# print(House_1.street)
# print(House_2.number)
#
# House_1.build()
#
# print(House_1.age)
#
# House_1.age_of_house(5)
# print(House_1.age)

# наследования
class ProspectHouse(House):
    """ house on the prospect"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse('Lenina', 5)
print(PrHouse.prospect)
