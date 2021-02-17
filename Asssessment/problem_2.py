import pickle
from typing import Any


# Case 1


class Person(object):
    """ This class Instance can be pickled """

    def __init__(self, name) -> None:
        self.name = name

    def __getattribute__(self, name: str) -> Any:
        return object.__getattribute__(self, name)


p1 = Person('Russum')
print('\npickle.dumps(p1):', pickle.dumps(p1))


# Case 2  - PROBLEM
class Person(object):
    """ This class Instance can NOT be pickled """

    def __init__(self, name) -> None:
        self.name = name

    def __getattribute__(self, name: str) -> Any:
        return super(object, self).__getattribute__(name)


p1 = Person('Russum')
try:
    pickle.dumps(p1)
except TypeError as ex:
    print('\n', ex)


# Case 3 - SOLUTION
class Person(object):
    """ This class Instance can NOT be pickled """

    def __init__(self, name) -> None:
        self.name = name

    def __getattribute__(self, name: str) -> Any:
        return super(Person, self).__getattribute__(name)


p1 = Person('Russum')
print('\npickle.dumps(p1):', pickle.dumps(p1))
