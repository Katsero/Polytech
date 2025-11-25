class LinkedList():
    def __init__(self,array):
        self.head = None
        self.tail = None
        for element in array:
            self.newAppend(element)
        
    def newAppend(self, value):
        self.newInsert(-1, value)

# Ошибки
    def loor(self): #List out of range
        print('Индекс списка вне допустимого диапазона')
    def enf(self): #Element not found
        print('Элемент не найден')
    def lie(self): #List is empty
        print('Список пуст')

    def newInsert(self, index, value):
        if index < 0:
            if index == -1:
                if self.tail:
                    # self.tail.next = self.tail = Node(value, None, self.tail) #???
                    self.tail = Node(value, None, self.tail)
                    self.tail.prev.next = self.tail
                else:
                    self.head = self.tail = Node(value)
                return

            current = self.tail
            while current:
                if index == -2:
                    if current.prev:
                        current.prev = Node(value, current, current.prev)
                        current.prev.prev.next = current.prev
                    else:
                        self.head = Node(value, self.head)
                        self.head.next.prev = self.head
                    return
                index += 1
                current = current.prev
            self.loor()

        
        else:
            if index == 0:
                if self.head:
                    self.head = Node(value, self.head)
                    self.head.next.prev = self.head
                else:
                    self.head = self.tail = Node(value)
                return
            
            current = self.head
            while current:
                if index == 1:
                    if current.next:
                        current.next = Node(value, current.next, current)
                        current.next.next.prev = current.next
                    else:
                        self.tail = Node(value,None,self.tail)
                        self.tail.prev.next = self.tail
                    return
                index -= 1
                current = current.next
            self.loor()

    def newPop(self, index = -1):
        if index < 0:
            if index == -1:
                if self.tail:
                    if self.tail != self.head:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        self.head = self.tail = None
                    return
            current = self.tail
            while current:
                if index == 0:
                    if current.prev:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                    else:
                        self.tail = current.next
                        current.next.prev = None
                    return
                current = current.prev
                index += 1
            self.loor()

        else:
            if index == 0 and self.head:
                self.head = self.head.next
                self.head.prev = None
                return
                
            current = self.head
            while current:
                if index == 0:
                    if current.next:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev
                        current.prev.next = None
                    return
                current = current.next
                index -= 1
            self.loor()

# Первый попавшийся совпадающий элемент
    def newRemove(self,value):
        if not self.head:
            self.loor()
            return
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        while current: 
            if current.value == value:
                if current.next:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                else:
                    self.tail = current.prev
                    self.tail.next = None
                return
            current = current.next
        self.enf()

    def searchIndex(self, index):
        if index < 0:
            current = self.tail
            while current:
                if index == -1:
                    print(current.value)
                    return
                index += 1
                current = current.prev
            self.loor()
        
        else:
            current = self.head
            while current:
                if index == 0:
                    print(current.value)
                    return
                index -= 1
                current = current.next
            self.loor()

    def searchValue(self,value):
        current = self.head
        res = LinkedList([])
        index = 0
        while current:
            if current.value == value:
                res.newAppend(index)
            index += 1
            current = current.next
        
        if res.head:
            res.output()
        else:
            self.enf()



    def output(self):
        if not self.head:
            self.lie()
            return
        
        res = '['
        current = self.head
        while current.next:
            res += str(current.value)
            res += ', '
            current = current.next
        res += str(current.value)
        res += ']'
        print(res)

class Node():
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev


#ТЕСТЫ
new = LinkedList([1,2,3,4])
new.newAppend('bye')
new.output()
print('________')
new.newInsert(4, 5)
new.newInsert(2, 3)
new.newInsert(3, 2)
new.output()
print('________')
new.newInsert(-5,0)
new.output()
print('________')
new.newInsert(1000,'aboba')
new.newInsert(-1000,'aboba')
new.output()
print('________')
new.newPop()
new.newPop(2)
new.newPop(-2)
new.output()
print('________')
new.newPop(1000)
new.newPop(-1000)
new.output()
print('________')
new.newRemove(2)
new.newRemove(4)
new.newRemove('aboba')
new.output()
print('________')
new.searchIndex(2)
new.searchIndex(-2)
new.searchIndex(0)
new.searchIndex(-1)
new.searchIndex(100)
new.searchIndex(-100)
print('________')
new.newInsert(2,2)
new.newInsert(2,2)
new.newInsert(0,0)
new.output()
print('________')
new.searchValue(0)
new.searchValue(1)
new.searchValue(2)
new.searchValue(5)
new.searchValue('aboba')
print('________')
# Пустые тесты
new = LinkedList([])
new.newRemove(0)
new.newRemove(-1)
new.newPop(0)
new.newPop(-1)

new.newInsert(-1,0)
new.newPop()
new.newInsert(0,0)
new.newPop()

new.output()
print('________')