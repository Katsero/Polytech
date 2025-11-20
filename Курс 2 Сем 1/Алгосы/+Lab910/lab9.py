# Валидация ввода
def lineInput():
    newline = ''
    while newline == '':
        line = input("Введите строку состоящую из скобок: ")

        valid = True
        allowed = ['(',')','[',']','{','}']

        for letter in line:
            if letter not in allowed:
                valid = False
            else: 
                newline += letter

        if not valid:
            print(f'Строка была очищена: {newline}')

        if newline == '':
            print('Пустая строка не подойдёт')
        
    return newline

# Функции стека: stack <-> elem
# stack.pop()
# stack.append()

while True:
    line = lineInput()
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    # Иммитация ввода символов поштучно
    for element in line:

        if len(stack) > 0:
            if pairs[stack[-1]] == element:
                stack.pop()
                continue
        
        if element in pairs:
            stack.append(element)
        else:
            stack = [1]
            break
        
        
    print(f'Скобки в {line} {'парны' if len(stack)==0 else 'не парны'}')

    # if len(stack)==0:
    #     print(f'Скобки в {line} парны')
    # else:
    #     print(f'Скобки в {line} не парны')