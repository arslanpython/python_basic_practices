"""http://book.pythontips.com/en/latest/decorators.html#writing-your-first-decorator"""


def hi(name="yasoob"):
    def test():
        print("Nested Function")

    return test()

print(hi())


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


print(hi())
print('--> ', hi()())
a = hi()
print(a)
print(a())


# Simple Decorator
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)


# Now More usable of decorator

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

test = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

test()
print('-----   ---')
print(a_new_decorator(a_function_requiring_decoration))
a_new_decorator(a_function_requiring_decoration())  # only passed function executed
# a_new_decorator(a_function_requiring_decoration)()

print('\n\n')

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
print(a_function_requiring_decoration.__name__)

print('\n------------')

def name_decorator(func):
    def decorated(*args, **kwargs):
        if not can_run:
            return "Fucntion is not running"
        return func(*args, **kwargs)

    return decorated

can_run = True
@name_decorator
def name():
    return "Function is running"

print(name())
print(name.__name__)


print('\n------------')

'''Note: @wraps takes a function to be decorated and adds the functionality of copying over the function name, 
docstring, arguments list, etc. This allows us to access the pre-decorated function’s properties in the decorator. '''
from functools import wraps

def name_decorator(func):
    @wraps(func)   # instead of replacing name function with decorated its copying the function
    def decorated():
        return func

    return decorated

@name_decorator
def name():
    return "Function is running"

print(name.__name__)

print('\n------------')

def logit(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

result = addition_func(4)
print(result)


print('\n---------------')

def decorator_with_arguments(function):
    def wrapper_accept_arguments(arg1, arg2):
        arg1 = arg1.upper()
        arg2 = arg2.upper()
        print("City 1: {} ----  City 2: {}".format(arg1, arg2))
        # function(arg1, arg2)
        return function(arg1, arg2)

    return wrapper_accept_arguments

# @decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

# cities("Lahore", 'Karachi')
# OR
# decorator = decorator_with_arguments(cities)
# decorator("Lahore", "Bhimber")


print('\n -----------------')
def decorator_with_arguments(function):
    def wrapper_accept_arguments(arg1, arg2):
        arg1 = arg1.upper()
        arg2 = arg2.upper()
        print("City 1: {} ----  City 2: {}".format(arg1, arg2))
        # function(arg1, arg2)
        return function(arg1, arg2)

    return wrapper_accept_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("I am Cities Function")
    return "Cities I hate are {0} and {1}".format(city_one, city_two)

print(cities("bbbbbb", 'Karachi'))


print('\n**************')
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()


print('-'*10)
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")


def name_decorator(callback):
    def wrapper(name, *args):
        name = name.upper()
        print(f"Decorated Name: {name}")
        # callback(name)
        # return callback(name)
        return "Wrapper Return value"

    return wrapper

@name_decorator
def name(name):
    return f"My Name is {name}"

print('--------------------------')
print(name("alif arslan"))

print('/'*10)

def a_new_decorator(a_func):
    print('inside decorator')
    print(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    # print('---> ', a_function_requiring_decoration.__name__)
    print("I am the function which needs some decoration to remove my foul smell")

a_new_decorator(a_function_requiring_decoration())

print('*'*10)







