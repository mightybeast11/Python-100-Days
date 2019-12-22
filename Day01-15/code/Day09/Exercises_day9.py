# -*- coding:utf-8 -*-
# Author: Zihang


# Practice:
class Person(object):

    # 限定Person对象只能有_name, _age, _gender attributes
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # getter
    def name(self):
        return self._name

    @property  # getter
    def age(self):
        return self._age

    @age.setter  # setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} is watching piggy peggy')
        else:
            print(f'{self._name} is watching pornography')


def person_instance():
    person = Person('王大锤', 24)
    person.play()
    person.age = 15
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute. There is not setter for _name.
    person._gender = 'male'
    # person.is_gay = True
    print(person._gender)



if __name__ == '__main__':
    person_instance()
