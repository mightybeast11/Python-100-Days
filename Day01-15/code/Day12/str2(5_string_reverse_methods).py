"""
字符串常用操作 - 实现字符串倒转的方法

Version: 0.1
Author: 骆昊
Date: 2018-03-19
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    # StringIO对象是Python中的可变字符串
    # 不应该使用不变字符串做字符串连接操作 因为会产生很多无用字符串对象
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        # from the last element to the first (which is 0 but need to stop before -1, the step is -1)
        rstr.write(str[index]) # write into rstr from the last element of str
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))
    # The join() method provides a flexible way to concatenate string. Syntax: string.join(iterable)


def reverse_str5(str):
    # 将字符串处理成列表
    str_list = list(str)
    str_len = len(str)
    '''
    # 使用zip函数将两个序列合并成一个产生元组的迭代器.
    # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
    # iterator is paired together, and then the second item in each passed iterator are paired together etc.
    # If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
    # Syntax: zip(iterator1, iterator2, iterator3 ...)
    '''
    # 每次正好可以取到一前一后两个corresponding index来实现元素的交换
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # 将列表元素连接成字符串
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)
