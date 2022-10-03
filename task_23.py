"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
o [2, 3, 4, 5, 6] => [12, 15, 16];
o [2, 3, 5, 6] => [12, 15]

"""
def converting_list():
    list_value = input('Задайте список из нескольких чисел: ')
    list_value=list_value.replace(' ', ',')
    list_value=list_value.replace('.', ',')
    list_value=list_value.split(',')
    new_list_value = []
    for i in list_value:
        if i.isdigit()==True:
            new_list_value.append(int(i))
    return new_list_value

def multiply_first_last(value_list):
    list_reserv = value_list[::-1]
    new_lenght_even = len(value_list)//2
    new_lenght_odd = new_lenght_even+1
    if len(value_list)%2==0:
        value_list = value_list[:new_lenght_even]
        list_reserv = list_reserv[:new_lenght_even]
        multiply_even = list(map(lambda i,j:i*j, value_list, list_reserv))
    elif len(value_list)==1:
        multiply_even = value_list
    else:
        value_list = value_list[:new_lenght_odd]
        list_reserv = list_reserv[:new_lenght_odd]
        multiply_even = list(map(lambda i,j:i*j, value_list, list_reserv))
    return multiply_even

s = converting_list()
print(multiply_first_last(s))