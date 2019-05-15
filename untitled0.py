# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:12:45 2019

@author: roy
"""

from numpy.random import choice
from numpy import array
from numpy import array_equal
from numpy import intersect1d
trial_time = 10
digit = 4
answer = choice(range(10), digit, replace = False)
counter = 0
while True:
    counter += 1
    number = str(input('请输入0~9不重複的四位數: '))
    try:
        digit_number = array([int(x) for x in str(number)])
        if array_equal(answer, digit_number) == False:
            A = (digit_number == answer).sum()
            B = len(intersect1d(digit_number[(digit_number == answer) == False], answer[(digit_number == answer) == False]))
            print('%dA %dB' % (A, B))
        else:
            print('正確答案!')
            break
    except (ValueError, AttributeError):
        print('請輸入數字，且不重複的四位數')
print('你總共猜了%d次' % counter)
if counter > trial_time:
    print('你的運氣很不好ㄋㄟ')