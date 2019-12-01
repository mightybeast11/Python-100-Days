"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 骆昊
Date: 2018-02-26

请将该文件命名为hello.py

使用Windows的小伙伴可以在命令行提示下通过下面的命令运行该程序
python hello.py

对于使用Linux或macOS的小伙伴可以打开终端并键入下面的命令来运行程序
python3 hello.py
"""

print('hello, world!')
# print("你好,世界！")
# "" and '' is the same.
print('你好', '世界')

# sep: string inserted between values, default a space. end: string appended after the last value, default a newline.
print('hello', 'world', sep=', ', end='!')
# default end is a new line, but here it is altered to be a '!', so the next line is immediately after this print line.
print('goodbye, world', end='!\n')

print('1', '2', '3', sep='.', end='?')