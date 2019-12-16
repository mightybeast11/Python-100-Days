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


def is_palindrome(x):
    x_str = str(x)
    pair = len(x_str) // 2
    for i in range(pair):
        if x_str[i] != x_str[len(x_str) - 1 - i]:
            return False
    return True

# 3. prime


def is_prime(x):
    for factor in range(2, x):
        if x % factor == 0:
            return False
    return True if x != 1 else False


# 4. unfixed parameters: add * in front of the parameter.


def unfixed(*a):
    sum = 0
    for i in a:
        sum += i
    return sum



if __name__ == '__main__':
    print(gcd(3, 6))
    print(lcm(6, 3))
    print(is_palindrome(12321))
    print(is_palindrome(12323))
    print(is_palindrome(12345678999987654321))

    num = int(input('Please input an interger: '))
    if is_palindrome(num) and is_prime(num):
        print('%d is a prime palindrome.' % num)
    else:
        print('%d is not a prime palindrome.' % num)

    print(unfixed(1, 3, 5))
    print(unfixed(1, 2))