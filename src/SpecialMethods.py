class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    """The __str__ method in Python represents the class objects as a string – it can be used for classes.
    The __str__ method should be defined in a way that is easy to read and outputs all the members of the class."""

    def __str__(self):
        return f'{self.title} by {self.author}'

    """len(s) is a built - in Python method which returns the length of an object. Now __len__() is a special method that is internally
    called by len(s) method to return the length of an object."""

    def __len__(self):
        return self.pages

    """Destructors are called when an object gets destroyed.In Python, destructors are not needed as much needed in C + + because Python
    has a garbage collector that handles memory management automatically. The __del__() method is a known as a destructor
    method in Python.It is called when all references to the object have been deleted i.e when an object is garbage collected."""

    def __del__(self):
        print(f'{self.title} has been deleted !')


obj = Book(title='Python rocks', author='Brij', pages=700)
print('content of object : {}'.format(obj))
print('length of object : {}'.format(len(obj)))
del obj
# to check if the object is deleted
try:
    print('object : {}'.format(obj))
except:
    print('object deleted !')

"""
### OUTPUT ###
content of object : Python rocks by Brij
length of object : 700
Python rocks has been deleted !
object deleted !
"""
