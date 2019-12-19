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


# 4. find largest and second largest in a list


def max2(l):
    (m1, m2) = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for index in range(2, len(l)):
        if l[index] > m1:
            m2 = m1
            m1 = l[index]
        elif m2 < l[index] < m1:
            m2 = l[index]
    return (m1, m2)


# +2. Circle:
def circle():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30  # index will not exceed 30.
    for person in persons:
        print('基' if person else '非', end='')


# +3. #chess
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def chess():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = (choice == 'yes')



if __name__ == '__main__':
    print(generate_code())
    print(generate_code(5))
    l1 = [x for x in range(100)]
    print(max2(l1))
    # l2 = (x for x in range(100))   # generator can only be used for iteration so far.

# enumerate: iterate the index and content simultaneously.
    l3 = [x for x in range(10)]
    for index, elem in enumerate(l3):
        if index % 2 == 0:
            print(elem, end=" ")
    print()

    circle()

    chess()