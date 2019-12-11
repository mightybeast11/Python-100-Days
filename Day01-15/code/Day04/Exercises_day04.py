# -*- coding:utf-8 -*- 
# Author: Zihang

# 1. prime number
# number = int(input('Input an integer: '))
#
# status = True
# for trial_factor in range(2, number):
#     if number % trial_factor == 0:
#         status = False
#         break
# if not status:
#     print('%d is not a prime number, it is divisible by %d.' % (number, trial_factor))
# else:
#     print('%d is a prime number.' % number)

# 2. greatest common divisor & least common multiple
# x = int(input("Input x: "))
# y = int(input("Input y: "))
#
# status1 = False
# status2 = False
#
# if x <= y:
#     for trial_divisor in range(1, x):
#         if x % trial_divisor == 0 and y % trial_divisor == 0:
#             status1 = True
#             break
#
#     for trial_multiple in range(y, x * y + 1):
#         if trial_multiple % x == 0 and trial_multiple % y == 0:
#             status2 = True
#             break
# else:
#     for trial_divisor in range(1, y):
#         if x % trial_divisor == 0 and y % trial_divisor == 0:
#             status1 = True
#             break
#
#     for trial_multiple in range(x, x * y + 1):
#         if trial_multiple % x == 0 and trial_multiple % y == 0:
#             status2 = True
#             break
#
# if status1:
#     print('%d is the greatest common divisor of %d and %d' % (trial_divisor, x, y))
# if status2:
#     print('%d is the least common multiple of %d and %d' % (trial_multiple, x, y))

# 3. draw star
row = int(input('请输入行数: '))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='')  # end is empty string (not space), to keep pointer in the current line.
    print()  # move the pointer to the next line.

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()