""" 
24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from functools import reduce

a = [1.02, 1.23, 3.1, 5, 10.11]

res_a= []
for i in a:
    i = str(i)
    if i.find('.')!=-1:
        j=i.find('.')
        res_a.append('0'+i[j:])
res_b =[]

for j in res_a:
    res_b.append(float(j))
max_list = reduce(lambda i, j: i if(i>j) else j, res_b)
min_list = reduce(lambda i, j: i if(i<j) else j, res_b)
result = max_list-min_list
print(result)
    


