"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
o 45 -> 101101
o 3 -> 11
o 2 -> 10

"""
def conversion_binary (value):   #нет уточнения, какие числа переводим, функция только для целых чисел.
    result_list = []
    result = ''
    while value!=0:
        result_list.append(value%2)
        value=value//2 
    result_list = result_list[::-1]
    for j in result_list:
        result = result + str(j)
    return result

a=int(input('Введите число для преобразования в двоичную СИ: '))
print(int(conversion_binary(a)))