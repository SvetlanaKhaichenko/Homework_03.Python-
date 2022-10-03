'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
def fibonacci (n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def nega_fibonacci (n):
    if n ==0:
        return n
    else:
        return int((-1)**(n+1)*fibonacci(-n))

def print_fibonacci(n):

    result = []
    for i in range(-n, n+1):
        if i <=0:
            result.append(nega_fibonacci(i))
        else:
            result.append(fibonacci(i))
    return print(result)

value = int(input('Введите число: '))
print_fibonacci(value)


