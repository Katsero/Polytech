class LinkedList():
    def __init__(self,array):
        self.head = None
        self.tail = None
        for element in array:
            self.newAppend(element)
        
    def newAppend(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail = Node(value,None,self.tail)
            self.tail.prev.next = self.tail

# Ошибки
    def loor(self): #List out of range
        print('Индекс списка вне допустимого диапазона')
    def enf(self): #Element not found
        print('Элемент не найден')

    def newInsert(self, index, value):
        if index < 0:
            index += 1
            current = self.tail
            while current:
                if index == 0:
                    if current.prev:
                        current.prev = Node(value, current.prev, current)
                        current.prev.prev.next = current.prev
                    else:
                        self.head = Node(value, self.head)
                        self.head.next.prev = self.head
            self.loor()
        elif index == 0:
            self.head = Node(value, self.head)
        else:
            current = self.head
            while current:
                if index == 0:
                    if current.next:
                        current.next = Node(value, current.next, current)
                        current.next.next.prev = current.next
                    else:
                        self.tail = Node(value,None,self.tail)
                        self.tail.prev.next = self.tail
            self.loor()

    def newPop(self, index):
        pass

    def newRemove(self, value):
        pass

    def searchIndex(self, index):
        pass

    def searchValue(self, value):
        pass


    def output(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

#TODO newInsert
#TODO newPop
#TODO newRemove
#TODO searchIndex
#TODO searchValue

class Node():
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev