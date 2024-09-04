# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def square_sum(numbers):
    list1=[]
    for i in numbers:
        a = sum([i ** 2])
        
        list1.append(a)
    print(sum(list1))
    return
    # return sum(list1)

square_sum([1,2,2])

# %% 

def sum_of_squares(lst):
    return sum([i ** 2 for i in lst])

sum_of_squares([1,2,2])