#Импорт функции генерации случайных чисел
from random import randint

#Ввод данных
R = float(input("Введите радиус: "))

#Оформление + первая строка
space = "+------------------+"
print(space)
print("| R =", R)
print(space)

#Повторени 10 выстрелов
for _ in range(10):

    #Случайный выбор x и y
    x = randint(int(-1400000*R),int(1400000*R))/1000000
    y = randint(int(-1400000*R),int(1400000*R))/1000000
    print("| x =", x)
    print("| y =", y)
    
    #Условие по области
    if ((x**2 + y**2 <= R**2) and ((x > 0) == (y > 0))) or ((x > 0) != (y > 0) and (x <= R and x >= -R and y <= R and y >= -R)):
        print("| Попадает")
    else:
        print("| Не попадает")
    print(space)
