#Импорт функций из библиотеки math
from math import (log, e)

#Ввод значений
xbeg = float(input("Введите xbeg: "))
xend = float(input("Введите xend: "))
Dx = float(input("Введите Dx: "))

#оформление, первая линия
space = "+\t---\t|\t---"
print(space)
print("|\tX\t|\tY")
print(space)

#Цикл по x, от xbeg до xend с периодичностью в Dx
x = xbeg
while x <= xend:
    #Проверка на различные области графика и
    #подсчёт по соответствующим им формулам
    if x > 4 or x < -4: #Не входит в график
        y = "Нет значения"
    elif x < 0: #Область окружности
        y = (4-(x+2)**2)**0.5
    elif x < 0.5: # Область нулевой прямой
        y = 0
    elif x <= 2: #Область ln(x)/x
        y = log(x)/x
    else: #Оставшаяся область, единичной прямой
        y = 1
    print("|\t",x,"\t|\t",y)
    print(space)
    x += Dx
