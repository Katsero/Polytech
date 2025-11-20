#Отключены строки ввиду отсутствия необходимости конкретно в данной лабораторной
from time import *
# from random import *


#Function timer
def Timer(array,func):
    # start_time = time()
    print(func.__name__)
    array = func(array)
    print(array)
    # end_time = time()
    # print(end_time - start_time)
    return array

#Array creation
def ArrayCreate():
    length = 0
    print('Введите длину массива')
    while length <= 0:
        length = intinput()
    # array_range = 1000
    array = []
    for _ in range(length):
        print("Заполните массив числами")
        array.append(intinput())
    return sorted(array)

#int input
def intinput():
    number = None
    while number == None:
        number = input('Введите целое число: ')
        try:
            number = int(number)
        except:
            print('Неверное значение')
            number = None   
    return number

#Array search
def ArraySearch(array):
    print('Введите искомое число')
    number = intinput()
    res = []
    for i in range(len(array)):
        if array[i] == number:
            res.append(i)
        elif res:
                break
    if len(res) == 0:
        print('Нет такого числа в массиве')
    else:
        print(f"В массиве число {number} стоит на позициях {res}")
    return array

#Array binary search
def ArrayBinarySearch(array):
    print('Введите искомое число')
    number = intinput()
    res = []
    left = 0
    right = len(array)-1
    found = "Not found"

    while left <= right:
        mid = (left+right)//2
        if array[mid] < number:
            left = mid + 1
            continue
        elif array[mid] > number:
            right = mid - 1
            continue
        else:
            found = mid
            break

    if found == "Not found":
        print('Нет такого числа в массиве')
        return array


    while found > 0 and array[found-1] == number:
        found -= 1
    while found <= (len(array)-1) and array[found] == number:
        res.append(found)
        found += 1

    print(f"В массиве число {number} стоит на позициях {res}")
    return array

#Array insert
def ArrayInsert(array):

    print('Введите число для добавления в массив')
    number = intinput()

    for i in range(len(array)):
        if number <= array[i]:
            array = array[:i] + [number] + array[i:]
            return array
    array += [number]
    return array

#Array pop
def ArrayPop(array):
    print('Введите число для удаления всех искомых в массиве')
    number = intinput()
    newarr = []
    for x in array:
        if x != number:
            newarr += [x]
    return newarr


array = []
array = ArrayCreate()
functions = [ArraySearch, ArrayInsert, ArrayPop, ArrayBinarySearch]
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
    array = Timer(array,current_func)
    print('-------------------')
