def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before the original function')
        original_func()
        print('some extra code, after the original function')

    return wrap_func()


@new_decorator
def func_needs_decorator():
    print('I need decorator !')
