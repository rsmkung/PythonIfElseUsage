# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 23:08:39 2018

@author: Sheng-Miao
"""

country = input('Which country are you from? ')
age = input('What is your age? ')
if (country == 'Taiwan'):
    if (int(age)>=18):
        print('You may have a driver license.', end='')
    else:
        print('You may not have a driver license.', end='')
elif (country == 'America'):
        if (int(age)>=16):
            print('You may have a driver license.', end='')
        else:
            print('You may not have a driver license.', end='')