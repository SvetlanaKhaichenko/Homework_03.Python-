""" 
24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from functools import reduce

def fractional(a):
    CONST = 1
    result = a%CONST
    return result

list_a = [1.1, 1.2, 3.1, 5.5, 10.11]
new_list_a = list(map(fractional, list_a))
min_list = reduce(lambda i, j:i if(i<j) else j, new_list_a)
max_list = reduce(lambda i, j:i if(i>j) else j, new_list_a)
result_differenc = max_list - min_list
result_differenc = str(result_differenc)
result_differenc = result_differenc[:4]
print(result_differenc)
print(new_list_a)
