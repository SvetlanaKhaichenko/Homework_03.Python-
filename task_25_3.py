
def conversion_binary_float(value):  # Перевод дробного десятичного числа в двоичную СИ, 6 знаков после запятой
    result_list = []
    result = ''
    binary_list = int(value)
    while binary_list != 0:
        result_list.append(binary_list % 2)
        binary_list = binary_list//2
    result_list = result_list[::-1]
    result_list.append(",")
    for j in result_list:
        result = result + str(j)
    a_float = value % 1
    res_float = ''
    while len(res_float) < 6:
        if a_float*2 >= 1:
            res_float += '1'
            a_float = a_float*2-1
        elif a_float == 0:
            break
        else:
            res_float += '0'
            a_float = a_float*2
    res_binary = result + res_float
    return res_binary


a = input('Введите число для преобразования в двоичную СИ: ')
a = a.replace(',', '.')
a = float(a)

print(conversion_binary_float(a))
