"""
写文本文件
将100以内的素数写入到文件中

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

from math import sqrt


def is_prime(n):
    assert n > 1  # negative n will always be considered prime after the following process
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


filenames = ('a.txt', 'b.txt', 'c.txt')  # a tuple
fs_list = []
try:
    for filename in filenames:
        fs_list.append(open(filename, 'w', encoding='utf-8')) # each element in this list is a file, which can be edited
    for num in range(2, 10000):
        if is_prime(num):
            if num < 100:
                fs_list[0].write(str(num) + '\n')
            elif num < 1000:
                fs_list[1].write(str(num) + '\n')
            else:
                fs_list[2].write(str(num) + '\n')
except IOError as ex:
    print(ex)
    print('写文件时发生错误!')
finally:
    for fs in fs_list:
        fs.close()
print('操作完成！')

# add some more in the first file
with open('a.txt', 'a') as f:
    for num in range(100, 999):
        if is_prime(num):
            f.write(str(num) + '\n')
print('写入完成!')
