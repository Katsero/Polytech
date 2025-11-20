class LinkedList():
    def __init__(self,array=[]):
        self.head = None
        for elem in array:
            self.newAppend(elem)

    def newAppend(self, value):
        current = self.head
        if not self.head:
            self.head = Node(value)
        else: 
            while current.next:
                current = current.next
            current.next = Node(value)

    # ERRORS
    def loor(self): #List out of range
        print('Индекс списка вне допустимого диапазона')
    def endstart(self):
        print('Однонаправленный список не поддерживает работу с конца')
    def enf(self): #Element not found
        print('Элемент не найден')

    def newInsert(self,index,value):
        if index < 0:
            self.endstart()
            return
        if index == 0:
            self.head = Node(value,self.head)
            return
            
        current = self.head
        while current:
            if index == 1:
                current.next = Node(value,current.next)
                return
            else:
                index -= 1
                current = current.next
        self.loor()
                
    def newPop(self,index):
        if index < 0:
            self.endstart()
        else:
            if index == 0:
                if self.head:
                    self.head = self.head.next
                    return
                self.loor()
                
            current = self.head
            while current:
                if index == 1:
                    if current.next:
                        current.next = current.next.next
                    else:
                        self.loor()
                    return
                else:
                    index -= 1
                    current = current.next
            self.loor()

# Первый попавшийся совпадающий элемент
    def newRemove(self,value):
        if not self.head:
            self.loor()
            return
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        self.enf()
    
    def searchIndex(self,index):
        if index < 0:
            self.endstart()
            return
        
        current = self.head
        while current:
            if index == 0:
                return current.value
            else:
                index -= 1
                current = current.next
        self.loor()
        return 

    def searchValue(self,value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next
        self.enf()
        return 

    def output(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

## TODO optimisation with searchIndex(pop and insert)
## TODO optimisation with searchValue(remove)
## TODO loor через длину списка?

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# ТЕСТЫ
newList = LinkedList([1,2,3])
newList.newAppend(4)
newList.newInsert(3,5)
newList.output()
print('________')
newList.newInsert(40,5)
newList.output()
print('________')
newList.newInsert(-4,'hello')
newList.output()
print('________')
newList.newInsert(0,'bye')
newList.output()
print('________')
newList.newPop(4)
newList.output()
print('________')
newList.newRemove('bye')
newList.output()
print('________')
print(
newList.searchIndex(0)
,newList.searchIndex(3)
,newList.searchIndex(-5)
,newList.searchIndex(5)
)
print('________')
print(
newList.searchValue(1)
,newList.searchValue(4)
,newList.searchValue('bye')
,newList.searchValue(55)
)
