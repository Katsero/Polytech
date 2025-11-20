#Ввод данных
R = float(input())
x = float(input())
y = float(input())

#Условие по области
if ((x**2 + y**2 <= R**2) and ((x > 0) == (y > 0))) or ((x > 0) != (y > 0) and (x <= R and x >= -R and y <= R and y >= -R)):
    print("Попадает")
else:
    print("Не попадает")
