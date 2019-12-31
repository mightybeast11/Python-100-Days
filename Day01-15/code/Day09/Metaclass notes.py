# -*- coding:utf-8 -*- 
# Author: Zihang



# from https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python



# Creating classes dynamically

# type works this way:
# type(name of the class,
#      tuple of the parent class (for inheritance, can be empty),
#      dictionary containing attributes names and values)

MyShinyClass = type('MyShinyClass', (), {})  # create a new class named MyShinyClass
print(MyShinyClass)  # returns a class object
print(MyShinyClass())  # create an instance with the class



# The main purpose of a metaclass is to change the class automatically, when it's created.

# remember that `type` is actually a class like `str` and `int`
# so you can inherit from it
class UpperAttrMetaclass(type):
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't see this.
    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)

# Do it in the OOP way:
class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # reuse the type.__new__ method
        # this is basic OOP, nothing magic in there
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)

# You may have noticed the extra argument upperattr_metaclass. There is nothing special about it: __new__ always
# receives the class it's defined in, as first parameter. Just like you have self for ordinary methods which receive
# the instance as first parameter, or the defining class for class methods.
#
# Of course, the names I used here are long for the sake of clarity, but like for self, all the arguments have
# conventional names. So a real production metaclass would look like this:

class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)

# We can make it even cleaner by using super, which will ease inheritance (because yes, you can have metaclasses,
# inheriting from metaclasses, inheriting from type):

class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

