# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer(num):
        """ This should do smth that has a relationship with the class,
        but not smth that must but unique per instance! """

    @classmethod
    def instantiate_from_csv(cls):
        """ This should do smth that has a relationship with the class,
        but usually, those are used to manipulate different structures
        of data to initiate objects, like we have done with CSV"""


# However, those could be called from instances

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_csv()
