# -*- coding:utf-8 -*- 
# Author: Zihang

# 1. gcd && lcm


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)  # use // to produce an int.


# 2. palindrome


def palindrome(x):
    x_str = str(x)
    pair = len(x_str) // 2
    for i in range(pair):
        if x_str[i] != x_str[len(x_str) - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    print(gcd(3, 6))
    print(lcm(6, 3))
    print(palindrome(12321))
    print(palindrome(12323))
    print(palindrome(12345678999987654321))
