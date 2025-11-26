class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree():
    def __init__(self, arr = None):
        self.root = None
        for elem in arr:
            self.treeAppend(elem)

    # # ERRORS
    def enf(self):
        print('Element not found')

    def treeAppend(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return
                # if current.left
                current = current.left
                continue
            # if value >= current.value
            if not current.right:
                current.right = Node(value)
                return
            # if current.right
            current = current.right
            continue

# # Far not the best attempt of removal
    # def treeRemove(self, value):
    #     # # root check
    #     if not self.root:
    #         self.nef()
    #         return

    #     # # root removal
    #     if self.root.value == value:
    #         current = self.root.right
    #         if current:
    #             if current.left:
    #                 while current.left.left:
    #                     current = current.left
    #                 if current.left.right:
    #                     current.left, current.left.left, current.left.right, self.root = current.left.right, self.root.left, self.root.right, current.left
    #                     return
    #                 # if not current.left.right
    #                 current = current.left
    #                 current.left, current.right, self.root = self.root.left, self.root.right, self.root
    #                 return
    #             # if not current.left
    #             current.left, self.root = self.root.left, current
    #             return
    #         # if not self.root.right
    #         self.root = self.root.left
    #         return

    #     # # node removal
    #     current = self.root
    #     while current:
    #         if value < current.value:
    #             if current.left and current.left.value == value:
    #                 if current.left.left and current.left.right: # both nodes
    #                     if current.left.right.left:
    #                         while current.left.right.left.left:
    #                             pass
    #                         return
    #                     current.left, current.left.right.left = current.left.right, current.left.left
    #                     return
    #                 #if nodes lack
    #                 current.left = (current.left.left if current.left.left else current.left.right) #take existing one
    #             # if not current.left or not current.left.value == value
    #             current = current.left
    #             continue
    #         # if value > current.value
    #         if current.right and current.right.value == value:
    #             # TODO remove
    #             return
    #         # if not current.right or not current.right.value == value
    #         current = current.right
    #         continue


#TODO чёт всё сломалось, ссылки хуйни
    def treeRemove(self, value):
        if not self.root:
            self.enf()
            return
        
        # if root
        if self.root.value == value:
            if not self.root.left or not self.root.right: # if 0/1 node
                self.root = (self.root.left if self.root.left else self.root.right)
                return
            # if 2 nodes
            current = self.root.right
            if not current.left: # right is min
                self.root, current.left = current, self.root.left
                return
            while current.left.left: #Ищем, current.left - минимальный элемент, не имеет левого потомка (!)
                current = current.left
            current.left.left, current.left.right, current.left, self.root = current.left, self.root.left, self.root.right, current.left.right
            self.root, current.left.left, current.left.right, current.left = current.left.right, current.left, self.root.left, self.root.right
            return
            
        # if not root
        current = self.root
        while current:
            if value < current.value:
                if  current.left and current.left.value == value:
                    if not current.left.left or not current.left.right: # if 0/1 node
                        current.left = (current.left.left if current.left.left else current.left.right)
                        return
                    # if 2 nodes
                    minimal = current.left.right
                    if not minimal.left: #right is min
                        current.left,minimal.left = minimal, current.left.left
                    while minimal.left.left: # minimal.left будет минимальным
                        minimal = minimal.left
                    minimal.left.left, minimal.left.right, minimal.left, current.left = current.left.left, current.left.right, minimal.left.right, minimal.left
                current = current.left
            elif value > current.value:
                if  current.right and current.right.value == value:
                    if not current.right.left or not current.right.right: # if 0/1 node
                        current.right = (current.right.left if current.right.left else current.right.right)
                        return
                    # if 2 nodes
                    minimal = current.right.right
                    if not minimal.left: #right is min
                        current.right,minimal.left = minimal, current.right.left
                    while minimal.left.left: # minimal.left будет минимальным
                        minimal = minimal.left
                    minimal.left.left, minimal.left.right, minimal.left, current.right = current.right.left, current.right.right, minimal.left.right, minimal.left
                    return
                current = current.right
        self.enf()
        return
            
# # поиск в ширину, итеративный
    def searchWidthIter(self,value):
        queue = [self.root]
        res = []
        while queue:
            if queue[0].value == value:
                res.append(queue[0])
                
            for element in [queue[0].left,queue[0].right]:
                if element:
                    queue.append(element)
            queue.pop(0)
        print(f'Элемент найден в древе, {res}')
            

# # поиск в ширину, рекурсивный
    def searchWidthRec():
        pass
    
# # поиск в глубину, итеративный
    def searchDepthIter1():
        pass
    
# # поиск в глубину, рекурсивный
    def searchDepthRec1():
        pass
    
# # поиск в глубину, итеративный
    def searchDepthIter2():
        pass
    
# # поиск в глубину, рекурсивный
    def searchDepthRec2():
        pass
    
# # поиск в глубину, итеративный
    def searchDepthIter3():
        pass
    
# # поиск в глубину, рекурсивный
    def searchDepthRec3():
        pass
# # Far not the best attempt of output
    # def treeOutput(self, node = None, depth = 0, res=[]):
    #     if depth == 0:
    #         node = self.root

    #     if not res[depth]:
    #         res[depth] = []

    #     if node:
    #         res[depth].append(node.value)
    #         res = self.treeOutput(node.left,depth,res)
    #         res = self.treeOutput(node.right,depth,res)
        
    #     if depth == 0:
    #         print(res)
    #     else:
    #         return(res)
        
    def treeOutput(self, node=None, depth=0):
        
        if depth == 0:
            print('tree:')
            node = self.root

        if node:
            print("  "*depth, node.value)
            self.treeOutput(node.right, depth+1)
            self.treeOutput(node.left, depth+1)
        
        if depth == 0:
            print('-------')

newTree = Tree([23, 87, 5, 64, 91, 12, 76, 34, 45, 89])
print('created')
newTree.treeOutput()
newTree.treeRemove(23)
newTree.treeOutput()
newTree.treeRemove(87)
newTree.treeOutput()