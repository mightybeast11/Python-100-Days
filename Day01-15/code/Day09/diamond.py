"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class A:

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()


# Method Resolution Order: defines the class search path used by Python to search for the right
    # method to use in classes having multi-inheritance.
if __name__ == '__main__':
    print(D.mro())
    # mro is [D, B, C, A, object]
    d = D()
    d.foo()
    # 'foo fo C'. Class D does not have foo method, so method from superclass C is applied.

    print(E.mro())
    # mro is [E, D, B, C, A, object]
    e = E()
    e.foo()
    # 'foo in E'. Line 35.
    # 'foo fo C'. In mro order, D and B do not have the method, so method from C is applied.
    # 'foo fo C'. In mro order, B does not have the method, so method from C is applied.
    # 'foo of A'. In mro order, method from A is applied.
