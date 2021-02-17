#!/usr/bin/python

class MySingleton(object):
    """ This is a singelton class"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._singleton = super(MySingleton, cls).__new__(
                cls, *args, **kwargs)
        return cls._singleton


# Instantiation is done only once, and
# subsequent instatiations will reuse existing instance
l1 = MySingleton()
l2 = MySingleton()

print('id(l1) == id(l2) :', id(l1) == id(l2))

assert l1 is l2
