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

# Функции очереди: elem -> queue -> elem
# queue.pop()
# queue.insert(0)

def pseudoStackAppend(queue, element):
    queue.insert(0,element)
    for _ in range(len(queue)-1):
        queue.insert(0,queue.pop())


while True:
    line = lineInput()
    pairs = {'(':')', '[':']', '{':'}'}
    queue = []

    # Иммитация ввода символов поштучно
    for element in line:

        if len(queue) > 0:
            if pairs[queue[-1]] == element:
                queue.pop()
                continue
        
        if element in pairs:
            # queue.append(element)
            pseudoStackAppend(queue,element)
        else:
            queue = [1]
            break
        
        
    print(f'Скобки в {line} {'парны' if len(queue)==0 else 'не парны'}')

    # if len(queue)==0:
    #     print(f'Скобки в {line} парны')
    # else:
    #     print(f'Скобки в {line} не парны')