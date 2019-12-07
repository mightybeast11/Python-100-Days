# -*- coding:utf-8 -*- 
# Author: Zihang

# # centigrade
# f = float(input('请输入华氏度：'))
# c = (f - 32) / 1.8
# print('%f 华氏度等于 %f 摄氏度' % (f, c))
# print('%.2f 华氏度等于 %.2f 摄氏度' % (f, c))

# # circle
# import math
# r = float(input('Input the radius: '))
# perimeter = 2 * r * math.pi
# area = math.pi * r ** 2
# print('周长为%.2f' % perimeter)
# print('面积为%.2f' % area)

# leap year: silly point, division produces float only, must use % to get modulo.
y = int(input('Input a year: '))
if (y % 4 == 0 and (y % 100 != 0)) or (y % 400 == 0):
    print('%d is a leap year' % y)
else:
    print('%d is not a leap year' % y)
