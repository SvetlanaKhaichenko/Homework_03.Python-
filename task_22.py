""" 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

''' Первый способ решения:
def sum_number_odd (list_user_value):
    sum_odd = 0
    START = 1
    STEP = 2
    for i in range(START,len(list_user_value),STEP):
        sum_odd += int(list_user_value[i])   
    return sum_odd
user_value = input('Задайте список из нескольких чисел через запятую: ')
user_value = user_value.split(',')
print(sum_number_odd(user_value))
'''

"""Второй способ решения"""
from functools import reduce

def converting_list():
    list_value = input('Задайте список из нескольких чисел: ')
    list_value=list_value.replace(' ', ',')
    list_value=list_value.replace('.', ',')
    list_value=list_value.split(',')
    new_list_value = []
    for i in list_value:
        if i.isdigit()==True:
            new_list_value.append(int(i))
    new_list_value = new_list_value[1:len(new_list_value):2]
    return new_list_value
    
sum_odd = reduce(lambda count,i:count+i, converting_list())
print(sum_odd)

