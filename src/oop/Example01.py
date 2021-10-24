"""The __init__ method is similar to constructors in C++ and Java.
Constructors are used to initialize the object’s state.
The task of constructors is to initialize(assign values) to the
data members of the class when an object of class is created.
Like methods, a constructor also contains collection of statements(i.e. instructions)
that are executed at time of Object creation. It is run as soon as an object of a class
is instantiated. The method is useful to do any initialization you want to do with your object."""


class Animal:
    def __init__(self, species, legs, spots):
        self.species = species
        self.legs = legs
        self.spots = spots

    def animal_details(self):
        print('animal {} has {} legs with {} spots on the body'.format(self.species, self.legs, self.spots))


animal_obj = Animal(species='tiger', legs=4, spots=True)
animal_obj.animal_details()
