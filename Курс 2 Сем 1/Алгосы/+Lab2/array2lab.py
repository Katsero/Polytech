from random import *

#Array creation
def ArrayCreate():
    length = 0
    print('Введите длину массива')
    while length <= 0:
        length = intinput()
    array_range = 1000
    array = []
    for _ in range(length):
        array.append(randint(-array_range, array_range))
    return array

#int input
def intinput():
    number = False
    while not number:
        number = input('Введите число: ')
        try:
            number = int(number)
        except:
            print('Неверное значение')
            number = False
    return number


#Array search
def ArraySearch(array):
    print('Введите искомое число')
    number = intinput()
    res = []
    for i in range(len(array)):
        if number == array[i]:
            res += [i]
    print(f"В массиве число {number} стоит на позициях {res}")
    return array    

#Array insert
def ArrayInsert(array):
    print('Введите число для добавления в массив')
    number = intinput()
    array += [number]
    return array

#Array pop
def ArrayPop(array):
    print('Введите число для удаления всех искомых в массиве')
    number = intinput()
    length = len(array)
    for i in range(length):
        if array[length-1-i] == number:
            array.pop(length-1-i)
    return array
            

array = []
array = ArrayCreate()
functions = [ArraySearch, ArrayInsert, ArrayPop]
functions_names = [i.__name__ for i in functions]
while True:
    print(f'Текуший массив: {array}')
    while True:
        print(f'Доступные функции: {functions_names}')
        current_func = input('Введите функцию: ')
        if current_func in functions_names:
            current_func = functions[functions_names.index(current_func)]
            break
        print('Неверная функция')
    array = current_func(array)
    print('-------------------')
