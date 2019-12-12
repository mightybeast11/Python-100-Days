# -*- coding:utf-8 -*- 
# Author: Zihang

# 1.1 Narcissus number
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
# 例如：$1^3 + 5^3+ 3^3=153$.
# for num in range(100, 1000):
#     if (num // 100) ** 3 + (num // 10 % 10) ** 3 + (num % 10) ** 3 == num:
#         print(num)

# 1.2 Reverse
# reversed_num = 0
# num = int(input('Input an integer: '))
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

# 2. Buy chicken
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y  # 100 chicken
#         if 5 * x + 3 * y + z / 3 == 100:  # 100 yuan
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# 3. Craps gambling: we only play 1 round here.
# import random
# dice1 = random.randrange(1, 7)
# print(dice1)
# dice2 = random.randrange(1, 7)
# print(dice2)
# first_roll = dice1 + dice2
# print(first_roll)
# print()
#
# if first_roll == 7 or first_roll == 1:
#     print('Player wins.')
#
# elif first_roll == 2 or first_roll == 3 or first_roll == 12:
#     print('Banker wins.')
#
# else:
#     print("Continue: ")
#     print()
#     next_roll = 0
#     while next_roll != 7 and next_roll != first_roll :
#         dice1 = random.randint(1, 7)
#         print(dice1)
#         dice2 = random.randint(1, 7)
#         print(dice2)
#         next_roll = dice1 + dice2
#         print(next_roll)
#         print()
#         if next_roll == 7:
#             print('Banker wins.')
#         elif next_roll == first_roll:
#             print('Player wins.')

# 4. Fibonacci: the key is (a, b = b, a + b), this will make the iteration much simpler and straightforward.
# first = 1
# second = 1
# print(first, end=' ')
# print(second, end=' ')
#
# for i in range(3, 21):
#     print(first + second, end=' ')
#     intermediate = first
#     first = second
#     second += intermediate

# 5. Perfect number
# import math
# for i in range(1, 10001):  # the target number range
#     sum = 1
#     inter = int(math.sqrt(i))
#     for j in range(2, inter + 1):  # checking each possible divisor
#         if i % j == 0:
#             sum += j
#             sum += (i // j)
#     if i == 1:
#         print(i)
#     elif sum == i:
#         print(i)

# 6. Prime numbers under 100
for p in range(2, 101):
    status = True
    for trial_factor in range(2, p):
        if p % trial_factor == 0:
            status = False
            break
    if status:
        print(p, end=' ')