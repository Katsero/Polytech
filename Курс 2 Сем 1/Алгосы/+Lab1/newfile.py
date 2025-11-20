x = input("Введите координату x: ")
y = input("Введите координату y: ")

try:
    x = float(x)
    y = float(y)
    if x == 0 or y == 0:
        raise ValueError()
except Exception:
    print('Введенные значения не числа или точка не лежит ни в одной из четвертей')
    exit()

if x > 0:
    if y > 0:
        print('1 четверть')
    else:
        print('4 четверть')
else:
    if y > 0:
        print('2 четверть')
    else:
        print('3 четверть')
