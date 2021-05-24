from django.template import Template, Context
from django.utils.safestring import SafeString

class Person:
    _CONST_LITERAL_NAME = 50

    def __init__(self, name, birth_day):
        self._name = name
        self._birth_day = birth_day

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def birth_day(self):
        return self._birth_day


if __name__ == '__main__':
    p = Person(name='Alex', birth_day=12)
    print(p.name)