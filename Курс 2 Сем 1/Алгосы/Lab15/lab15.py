from time import *
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
    def __init__(self, tree = None, maximal = True):
        self.maximal = maximal
        self.tree = []
        if tree:
            for element in tree:
                self.pyramideAppend(element)


    # ERRORS
    def enf(self,value = None):
        print(f"Element {value} not found")
        return
    def tie(self):
        print(f'Tree is empty')
        return
    def loor(self):
        print(f'List out of range')
        return

    # Tree immitation
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
    

    # Main functions
    def pyramideAppend(self, value):
        if not self.maximal:
            value = -value
            
        self.tree += [value]
        
        newIndex = len(self.tree)
        while self.findParentIndex(newIndex) is not None:
            parentIndex = self.findParentIndex(newIndex)
            if self.tree[newIndex - 1] <= self.tree[parentIndex - 1]:
                break
            self.tree[newIndex - 1], self.tree[parentIndex - 1] = self.tree[parentIndex - 1], self.tree[newIndex - 1]
            newIndex = parentIndex 

    def pyramideRemove(self,value):
        if not self.tree:
            self.enf(value)
            return    

        value = value if self.maximal else -value
        
        queue = [1]
        res = None
        while queue:
            current = queue.pop(0)
            if self.tree[current-1] == value:
                res = current
                break

            if self.findLeftChildIndex(current):
                queue.append(self.findLeftChildIndex(current))
            if self.findRightChildIndex(current):
                queue.append(self.findRightChildIndex(current))

        value = value if self.maximal else -value
        if res != None:
            self.tree[res-1] = self.tree[-1]
            self.tree.pop()
            self.pyramideRearrange(res)
        else:
            self.enf(value)
    
    def pyramidePop(self, index = 0):
        if not self.tree:
            self.loor()
            return

        if len(self.tree) <= index:
            self.loor()
            return
        
        if index + 1 == len(self.tree):
            return self.tree.pop()

        head, self.tree[index] = self.tree[index], self.tree[-1]
        self.tree.pop()
        self.pyramideRearrange(index+1)
        return head
        
    def pyramideRearrange(self, parentIndex):
        leftChildIndex = self.findLeftChildIndex(parentIndex)
        if leftChildIndex and self.tree[parentIndex-1] < self.tree[leftChildIndex-1]:
            self.tree[parentIndex-1], self.tree[leftChildIndex-1] = self.tree[leftChildIndex-1], self.tree[parentIndex-1]
            self.pyramideRearrange(leftChildIndex)
        rightChildIndex = self.findRightChildIndex(parentIndex)
        if rightChildIndex and self.tree[parentIndex-1] < self.tree[rightChildIndex-1]:
            self.tree[parentIndex-1], self.tree[rightChildIndex-1] = self.tree[rightChildIndex-1], self.tree[parentIndex-1]
            self.pyramideRearrange(rightChildIndex)

    def pyramideSearch(self,value):
        if not self.tree:
            self.enf(value)
            return    

        value = value if self.maximal else -value
        
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

        value = value if self.maximal else -value
        if res:
            print(f'Elemement {value} found at {res} positions')
        else:
            self.enf(value)

    # Output (obviously)
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
        print('    '*depth, self.tree[index-1] if self.maximal else -self.tree[index-1])
        if self.findLeftChildIndex(index):
            self.pyramideOutput(self.findLeftChildIndex(index), depth + 1)

        if depth == 0:
            print('-------')
        
    # Sort
    def pyramideSort(self):
        res = []
        while self.tree:
            
            head = self.pyramidePop()
            res.append(head if self.maximal else -head)
        return res


# newPyramide = Pyramide([45,2,16,19,81,54,47,15,65])
arr = arrayCreate()

## max
newPyramide = Pyramide(arr)
newPyramide.pyramideOutput()
print('-------')
newPyramide.pyramideSearch(newPyramide.tree[4])
newPyramide.pyramideSearch(46064)
newPyramide.pyramideOutput()
print('-------')
newPyramide.pyramideRemove(newPyramide.tree[0])
newPyramide.pyramideRemove(46064)
newPyramide.pyramideOutput()
print('-------')

## min
newPyramide = Pyramide(arr, False)
newPyramide.pyramideOutput()
print('-------')
newPyramide.pyramideSearch(-newPyramide.tree[4])
newPyramide.pyramideSearch(46064)
newPyramide.pyramideOutput()
print('-------')
newPyramide.pyramideRemove(-newPyramide.tree[0])
newPyramide.pyramideRemove(46064)
newPyramide.pyramideOutput()
print('-------')

## empty
newPyramide = Pyramide()
newPyramide.pyramideOutput()
newPyramide.pyramideRemove(46064)
newPyramide.pyramideSearch(46064)
print('-------')

## head only
newPyramide = Pyramide([5])
newPyramide.pyramideOutput()
newPyramide.pyramideSearch(46064)
print('-------')


## sort
newPyramide = Pyramide(arr)
newPyramide.pyramideOutput()
sortedArr = newPyramide.pyramideSort()
print(sortedArr)

## sort min
newPyramide = Pyramide(arr, False)
newPyramide.pyramideOutput()
sortedArr = newPyramide.pyramideSort()
print(sortedArr)


#Function timer
def Timer(array,func,number):
    start_time = time()
    print(func.__name__)
    func(array[::],number)
    end_time = time()
    print(end_time - start_time)
# TODO:
# c: время выполнения