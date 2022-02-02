class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('tim')
p2 = Person('jill')
print(Person.number_of_people_())


# print(Person.number_of_people)
#
# p1 = Person('tim')
# p2 = Person('jill')
# Person.number_of_people = 8
#
# Person.number_of_people = 9
# print(p1.number_of_people)
#
#
# print(Person.number_of_people)

# p1 = Person('tim')
# print(Person.number_of_people)
# p2 = Person('jill')
# print(Person.number_of_people)


