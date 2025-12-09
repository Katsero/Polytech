from time import *
from random import *

# импорт пирамидок из 15 лабы
import sys
import os

# Добавляем путь к папке Lab15 в sys.path
lab15_path = os.path.join(os.path.dirname(__file__), '..', '+Lab15')
sys.path.append(lab15_path)

from lab15 import Pyramide # type: ignore

def pyraSort(newPyramide):
    return newPyramide.pyramideSort()

#Function timer
def Timer(array,func): #TODO оптимизация на результат
    print(func.__name__)
    start_time = time()
    print(func(array[::]))
    end_time = time()
    print(end_time - start_time)

#Array creation
def ArrayCreate(length):
    ##РАЗМЕРНОСТЬ МАССИВА
    array_range = 1000
    array = []
    for _ in range(length):
        array.append(randint(-array_range, array_range))
    return array

#Bubble sort
def BubbleSort(array):
    length = len(array)
    for a in range(length):
        for b in range(length):
            if array[a] < array[b]:
                array[a], array[b] = array[b], array[a]
    return array

#Selection sort
def SelectionSort(array):
    length = len(array)
    for num in range(length):
        maximal = array[num]
        for pair in range(num,length):
            if maximal < array[pair]:
                maximal = array[pair]
                num = pair
        array.pop(num)
        array = [maximal] + array
    return array

#Insert sort
def InsertSort(array):
    length = len(array)
    for num in range(length):
        for checked in range(num):
            if array[num] <= array[checked]:
                array.insert(checked,array[num])
                array.pop(num+1)
                break
    return array

#Quick sort
def QuickSort(array):
    length = len(array)
    if length <= 1:
        return array
    
    center_index = length // 2
    center = array[center_index]
    index = 0

    
    for _ in range(length):
        if center_index > index:
            if array[index] <= center:
                array.insert(0,array[index])
                index += 1
            else: # > center
                array.append(array[index])
                center_index -= 1
            array.pop(index)
        elif center_index == index:
            index += 1
        else: #center_index < index
            if array[index] <= center:
                array.insert(0,array[index])
                index += 1
                array.pop(index)
                center_index += 1
            else: # > center
                array.append(array[index])
                array.pop(index)
                
    array = QuickSort(array[:center_index]) + [array[center_index]] + QuickSort(array[(center_index+1):])
    return array

#Merge sort
def MergeSort(array):
    
    #endpoint
    length = len(array)//2
    if length == 0:
        return array

    #recursion
    first_array = MergeSort(array[:length])
    second_array = MergeSort(array[length:])

    #merge sort
    array = []
    while first_array and second_array:
        if first_array[0] < second_array[0]:
            array.append(first_array[0])
            first_array.pop(0)
        else:
            array.append(second_array[0])
            second_array.pop(0)
    array += (first_array + second_array)

    return array

sorters = [BubbleSort,SelectionSort,InsertSort,QuickSort, MergeSort, pyraSort, sorted]
##sorters = [MergeSort] #Отладка
array = []
while not array:
    try:
        inp = int(input('Введите длину массива: '))
        array = ArrayCreate(inp)
        if int(inp) <= 0:
            print('Неверное значение')
            array = []
    except:
        print('Неверное значение')
        array = []
        
print(array)
for func in sorters:
    print('------------')
    if func == pyraSort:
        newPyramide = Pyramide(array)
        print(func.__name__)
        start_time = time()
        pyraSort(newPyramide)
        end_time = time()
        print(end_time - start_time)
    else:
        Timer(array[::],func)
