"""
从文本文件中读取数据

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import time


def main():

    # 一次性读取整个文件内容
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:  # finally clause is used to close the file, which is necessary.
        if f:
            f.close()

    print()  # separate the 2 copies

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        # 如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环
        # 境时自动释放文件资源.
        for line in f:
            print(line, end='')  # totally control the blank lines
            time.sleep(0.1)
            print()  # insert行距manually instead of the original ones
    print()

    # 读取文件按行读取到列表list中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
