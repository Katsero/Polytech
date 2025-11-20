#Импорт функции
from random import uniform

#Ввод данных
with open("Lab6_1_input.txt","r") as f:
    N = int(f.read())

#Создание массива со случайными числами
a = []
for _ in range(N):
    a.append(uniform(-5,5))

#Подсчёт нулей (№1) и суммы (№2.1)
zero = a.count(0)
s = sum(a[a.index(min(a))+1:])


#Сортировка (№2.2)
i = 0
while i < (len(a)-1):
    if abs(a[i]) < abs(a[i+1]):
        i += 1
    else:
        a[i], a[i+1] = a[i+1], a[i]
        i = 0

#Вывод результата
with open("Lab6_4_output.txt","w+") as f:
    ans = "Количество нулей:" + str(zero) + "\nСумма чисел после минимального:" + str(s) + "\nСписок, отсортированный в порядке возрастания модулей чисел:" + str(a)
    f.write(ans)
