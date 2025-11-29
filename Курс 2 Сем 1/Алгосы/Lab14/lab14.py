class Pyramide():
    def __init__(self, tree = None):
        self.tree = []
        for element in tree:
            self.pyramideAppend(element)

    def findParentIndex(self, index):
        if index == 0:
            return None
        return index//2
    
    def findLeftChildIndex(self, index):
        if (index * 2) > len(self.root):
            return None
        return index*2
    
    def findRightChildIndex(self, index):
        if ((index * 2)+1) > len(self.root):
            return None
        return (index*2) + 1

    def pyramideAppend(self,value):
        self.tree += [value]
        
        newIndex = len(self.tree)-1
        while self.findParentIndex(newIndex) != None:
             if not self.pyramideRearrange(newIndex):
                 break
             newIndex = self.findParentIndex(newIndex)

    def pyramideRearrange(self, childIndex):
        parentIndex = self.findParentIndex(childIndex)
        if self.tree[childIndex] > self.tree[parentIndex]:
            self.tree[childIndex], self.tree[parentIndex] = self.tree[parentIndex], self.tree[childIndex]
            return True
        return False
    
    def pyramideOutput(self):
        
        # Сделать вывод с правого поддрева -> корень -> левое поддрево
        #         10
        #     20
        #         15
        # 45
        #         10
        #     40
        #         35
        
        return self.tree