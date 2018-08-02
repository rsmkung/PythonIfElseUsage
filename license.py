# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:23:56 2018

@author: Sheng-Miao
"""

country = input('Which country are you from? ')
age = input('What is your age? ')
if ((country == 'Taiwan') and (int(age) >=18)) or ((country == 'America') and (int(age) >=16)):
    print('You may have a driver license.', end='')
else:
    print('You may not have a driver license.', end='')