from random import *
def arrayCreate(length = 11):
    ##РАЗМЕРНОСТЬ МАССИВА
    array_range = 100
    array = []
    for _ in range(length):
        array.append(randint(0, array_range))
        # array.append(randint(-array_range, array_range))
    return array
# Кусок с лабы 8

class Pyramide():
    def __init__(self, tree = None):
        self.tree = []
        if tree:
            for element in tree:
                self.pyramideAppend(element)

    # ERRORS
    def enf(self,value):
        print(f"Element {value} not found")
        return
    def tie(self):
        print(f'Tree is empty')
        return

    def findParentIndex(self, index):
        if index <= 1:
            return None
        return index//2
    
    def findLeftChildIndex(self, index):
        if (index * 2) > len(self.tree):
            return None
        return index*2
    
    def findRightChildIndex(self, index):
        if ((index * 2)+1) > len(self.tree):
            return None
        return (index*2) + 1

    def pyramideAppend(self,value):
        self.tree += [value]
        
        newIndex = len(self.tree)
        while self.findParentIndex(newIndex) != None:
             if not self.pyramideRearrange(newIndex):
                 break
             newIndex = self.findParentIndex(newIndex)

    def pyramideRearrange(self, childIndex):
        parentIndex = self.findParentIndex(childIndex)
        if self.tree[childIndex-1] > self.tree[parentIndex-1]:
            self.tree[childIndex-1], self.tree[parentIndex-1] = self.tree[parentIndex-1], self.tree[childIndex-1]
            return True
        return False
    
    def pyramideOutput(self, index = 1, depth = 0):
        
        # Вывод с правого поддрева -> корень -> левое поддрево
        #         10
        #     20
        #         15
        # 45
        #         10
        #     40
        #         35
        
        if not self.tree:
            self.tie()
            return

        if depth == 0:
            print('tree:')

        if self.findRightChildIndex(index):
            self.pyramideOutput(self.findRightChildIndex(index), depth + 1)
        print('    '*depth, self.tree[index-1])
        if self.findLeftChildIndex(index):
            self.pyramideOutput(self.findLeftChildIndex(index), depth + 1)

        if depth == 0:
            print('-------')

    def pyramideSearch(self,value):
        if not self.tree:
            self.enf(value)
            return    
        
        queue = [1]
        res = []
        while queue:
            current = queue.pop(0)
            if self.tree[current-1] == value:
                res.append(current-1)

            if self.findLeftChildIndex(current):
                queue.append(self.findLeftChildIndex(current))
            if self.findRightChildIndex(current):
                queue.append(self.findRightChildIndex(current))

        if res:
            print(f'Elemement {value} found at {res} positions')
        else:
            self.enf(value)
        
    def pyramideSort(self):
        # TODO
        res = []
        return res


# newPyramide = Pyramide([45,2,16,19,81,54,47,15,65])
newPyramide = Pyramide(arrayCreate())
newPyramide.pyramideOutput()
print(newPyramide.tree)
newPyramide.pyramideSearch(newPyramide.tree[4])
newPyramide.pyramideSearch('aboba')

newPyramide = Pyramide()
newPyramide.pyramideOutput()
newPyramide.pyramideSearch('aboba')

newPyramide = Pyramide([5])
newPyramide.pyramideOutput()
newPyramide.pyramideSearch('aboba')

# TODO:
# a: мин/макс пирамида - выбор, 
# b: удаление
# c: пирамидальная сортировка, время выполнения