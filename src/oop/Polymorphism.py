class Animal:
    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('i am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')

    def who_am_i(self):
        print('i am dog')


dog_obj = Dog()
dog_obj.who_am_i()
dog_obj.eat()

"""
### OUTPUT ###
animal created
dog created
i am dog
i am eating
"""
