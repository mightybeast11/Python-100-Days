# -*- coding:utf-8 -*- 
# Author: Zihang

# 2. 验证码
import random

caps = [chr(x + 65) for x in range(26)]
lower = [chr(x + 97) for x in range(26)]
num = [x for x in range(10)]


def random_caps():
    r = random.randrange(26)
    return caps[r]

def random_lower():
    r = random.randrange(26)
    return lower[r]

def random_num():
    r = random.randrange(10)
    return str(num[r])

def random_type():
    r = random.randint(0, 2)
    if r == 0:
        return random_caps()
    elif r == 1:
        return random_lower()
    elif r == 2:
        return random_num()


def generate_code(length=4):
    out = ''
    for _ in range(length):
        oneLetter = random_type()
        out += oneLetter
    return out


# 4. find largest second largenst in a list


def max2(l):
    (m1, m2) = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for index in range(2, len(l)):
        if l[index] > m1:
            m2 = m1
            m1 = l[index]
        elif m2 < l[index] < m1:
            m2 = l[index]
    return (m1, m2)


if __name__ == '__main__':
    print(generate_code())
    print(generate_code(5))
    l1 = [x for x in range(100)]
    print(max2(l1))
    # l2 = (x for x in range(100))   # generator can only be used for iteration so far.


