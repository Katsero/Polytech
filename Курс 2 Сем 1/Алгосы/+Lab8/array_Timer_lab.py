from time import *
from random import *


#Function timer
def Timer(array,func,number):
    start_time = time()
    print(func.__name__)
    func(array[::],number)
    end_time = time()
    print(end_time - start_time)

#Array creation
def ArrayCreate():
    length = 0
    while length <= 0:
        length = 100000
         #ДЛИННА МАССИВА
    array_range = 1000 #ДИАПАЗОН МАССИВА
    array = []
    for _ in range(length):
        array.append(randint(-array_range, array_range))
    return array


#Array search
def ArraySearch_unsorted(array,number):
    res = []
    for i in range(len(array)):
        if number == array[i]:
            res += [i]
    print(f"В массиве число {number} стоит на позициях {res}")
    return array    

#Array insert
def ArrayInsert_unsorted(array,number):
    array += [number]
    return array

#Array pop
def ArrayPop_unsorted(array,number):
    length = len(array)
    for i in range(length):
        if array[length-1-i] == number:
            array.pop(length-1-i)
    return array


#Array search
def ArraySearch_sorted(array,number):
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
def ArrayBinarySearch_sorted(array,number):
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
def ArrayInsert_sorted(array,number):
    for i in range(len(array)):
        if number <= array[i]:
            array = array[:i] + [number] + array[i:]
            return array
    array += [number]
    return array

#Array pop
def ArrayPop_sorted(array,number):
    newarr = []
    for x in array:
        if x != number:
            newarr += [x]
    return newarr

array = []
array = ArrayCreate()
number = array[randrange(0,len(array))]
#number = int(input())
print(f"Число с которым проводятся операции: {number}")
functions_unsorted = [ArraySearch_unsorted, ArrayInsert_unsorted, ArrayPop_unsorted]
functions_sorted = [ArraySearch_sorted, ArrayInsert_sorted, ArrayPop_sorted, ArrayBinarySearch_sorted]

print(f"Неотсортированный: {array}")
for func in functions_unsorted:
    print('------------')
    Timer(array[::],func,number)

array = sorted(array)

print(f"Отсортированный: {array}")
for func in functions_sorted:
    print('------------')
    Timer(array[::],func,number)
