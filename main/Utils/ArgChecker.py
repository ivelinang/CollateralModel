__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     ArgChecker.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for checking the input data for any
# class constructor
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type)+' but got '+str(type(value)))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate