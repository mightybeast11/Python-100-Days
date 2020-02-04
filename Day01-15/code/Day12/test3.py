"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')

    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    '''
    r'' raw string notation, contains 非转义的原始字符串. 以r开头的字符，常用于正则表达式，对应着re模块。
    ^                           start
    $                           end
    []                          anyone inside it
    [0-9a-zA-Z_]                anyone in 0-9, a-z, A-Z or _ 
    {6, 20}                     匹配至少6次至多20次
    '''

    # when string username does not follow the pattern, m1 is None, not None is true.
    if not m1:
        print('请输入有效的用户名.')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    '''
    [1-9]               pw cannot start with 0
    \d                  Matches any Unicode decimal digit. This includes [0-9], and also many other digit characters. 
                        In total, 5 to 12 digits where the first digit cannot be 0.
    '''

    if not m2:
        print('请输入有效的QQ号.')

    # print(m1)                 --> <re.Match object; span=(0, 9), match='weizihang'>
    # type(m1)                  --> <class 're.Match'>
    # type(m1 and m2)           --> <class 're.Match'>
    # type(bool(m1 and m2))     --> <class 'bool'>
    # print(bool(m1 and m2))    --> True
    if m1 and m2:
        print('你输入的信息是有效的!')


if __name__ == '__main__':
    main()
