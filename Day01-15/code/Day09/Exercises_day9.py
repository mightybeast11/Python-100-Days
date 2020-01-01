# -*- coding:utf-8 -*-
# Author: Zihang


# Class Practice:
class Person(object):

    # 限定Person对象只能有_name, _age, _gender attributes
    # Attributes are prefixed with _, to indicate that it should not be changed.
    # __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # attribute getter
    def name(self):
        return self._name

    @property  # attribute getter
    def age(self):
        return self._age

    @age.setter  # attribute setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


# Inheritance
class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._name} 学习了 {course}，取得了{self._grade}分.')


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._name}{self._title}正在讲 {course}.')


# Abstract class (Abstract method means the class cannot be instantiated.)
# Polymorphism
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):  # Abstract class, cannot be instantiated. Created to be inherited.

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):  # Instantiate the abstract class Pet.

    def make_voice(self):
        print(f'{self._nickname}:  汪汪汪。。。')

class Cat(Pet):  # Instantiate the abstract class Pet.

    def make_voice(self):
        print(f'{self._nickname}:  喵喵喵。。。')



if __name__ == '__main__':

    # Student subclass instance
    me = Student('Wei', 23, 83)
    me.study('Relational Database')

    # Teacher subclass instance
    t = Teacher('六花', 25, '会长')
    t.teach('Animation')

    # 上面的代码中，Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，当我们在main函数中调用该方法时，
    # 这个方法就表现出了多态行为（同样的方法做了不同的事情）。
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()