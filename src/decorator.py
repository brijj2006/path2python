"""A decorator is a design pattern in Python that allows a user
to add new functionality to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate."""


def new_decorator(original_func):
    def wrap_func(message):
        print('some extra code, before the original function')
        original_func(message)
        print('some extra code, after the original function')

    return wrap_func


@new_decorator
def func_needs_decorator(welcome):
    print('I need decorator - {}'.format(welcome))


func_needs_decorator('welcome to python !')
