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
            current.left.left, current.left.right, current.left, self.root = self.root.left, self.root.right, current.left.right, current.left
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

# # # ПОИСКИИИИ   
# # поиск в ширину, итеративный
    def searchWidthIter(self,value):
        queue = [self.root]
        while queue:
            if queue[0].value == value:
                print(f'Элемент найден в древе, {queue[0]}')
                return
                
            for element in [queue[0].left,queue[0].right]:
                if element:
                    queue.append(element)
            queue.pop(0)
        print('Элемент не найден в древе')
            
# # поиск в ширину, рекурсивный
    def searchWidthRec(self, value, queue = None, depth = 0):
        if not self.root:
            print('Элемент не найден в древе')
            return
        
        if depth == 0:
            queue = [self.root]
        
        newqueue = []
        for node in queue:
            if node.value == value:
                print(f'Элемент найден в древе, {node}')
                return
            if node.left:
                newqueue.append(node.left)
            if node.right:
                newqueue.append(node.right)
        
        if newqueue:
            self.searchWidthRec(value,newqueue, depth + 1)
        else:
            print('Элемент не найден в древе')

    
# # поиск в глубину, preorder, итеративный
    def searchPreorderIter(self, value):
        if not self.root:
            print('Элемент не найден в древе')
            return
        
        stack = [self.root]
        while stack:
            current = stack.pop(-1)
            if current.value == value:
                print(f'Элемент найден в древе, {current}')
                return

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print('Элемент не найден в древе')

# # поиск в глубину, preorder, рекурсивный
    def searchPreorderRec(self, value, current = None, depth = 0):
        if not self.root:
            print('Элемент не найден в древе')
            return False
        
        if depth == 0:
            current = self.root
        
        # центр
        if current.value == value:
            print(f'Элемент найден в древе, {current}')
            return True
        # лево        
        if current.left:
            first = self.searchPreorderRec(value, current.left, depth + 1)
        else:
            first = False
        # право
        if current.right:
            second = self.searchPreorderRec(value, current.right, depth + 1)
        else:
            second = False
        # результат
        if current == self.root and not first and not second:
            print('Элемент не найден в древе')
    
# # поиск в глубину, inorder, итеративный
    def searchInorderIter(self, value):
        if not self.root:
            print('Элемент не найден в древе')
            return
        
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.value == value:
                print(f'Элемент найден в древе, {current}')
                return
            
            current = current.right
        print('Элемент не найден в древе')

# # поиск в глубину, inorder, рекурсивный
    def searchInorderRec(self, value, current = None, depth = 0):
        if not self.root:
            print('Элемент не найден в древе')
            return
        
        if depth == 0:
            current = self.root

        if current.left:
            first = self.searchPreorderRec(value, current.left, depth + 1)
        else:
            first = False
        if current.value == value:
            print(f'Элемент найден в древе, {current}')
            return True        
        if current.right:
            second = self.searchPreorderRec(value, current.right, depth + 1)
        else:
            second = False       

        if current == self.root and not first and not second:
            print('Элемент не найден в древе')

# # поиск в глубину, postorder, итеративный
    def searchPostorderIter(self, value):
        if not self.root:
            print('Элемент не найден в древе')
            return
    
        stack_children = [self.root]
        stack_parent = []
        while stack_children:
            current = stack_children.pop()
            stack_parent.append(current)

            if current.left:
                stack_children.append(current.left)
            if current.right:
                stack_children.append(current.right)

        while stack_parent:
            current = stack_parent.pop()
            if current.value == value:
                print(f'Элемент найден в древе, {current}')
                return

        print('Элемент не найден в древе')

# # поиск в глубину, postorder, рекурсивный
    def searchPostorderRec(self, value, current = None, depth = 0):
        if not self.root:
            print('Элемент не найден в древе')
            return

        if depth == 0:
            current = self.root

        if current.left:
            first = self.searchPreorderRec(value, current.left, depth + 1)
        else:
            first = False
        if current.right:
            second = self.searchPreorderRec(value, current.right, depth + 1)
        else:
            second = False       
        if current.value == value:
            print(f'Элемент найден в древе, {current}')
            return True        

        if current == self.root and not first and not second:
            print('Элемент не найден в древе')
        
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

#1
print('1')
newTree.searchWidthIter(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchWidthIter('aboba')
#2
print('2')
newTree.searchWidthRec(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchWidthRec('aboba')

#3
print('3')
newTree.searchPreorderIter(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchPreorderIter('aboba')
#4
print('4')
newTree.searchPreorderRec(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchPreorderRec('aboba')

#5
print('5')
newTree.searchInorderIter(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchInorderIter('aboba')
#6
print('6')
newTree.searchInorderRec(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchInorderRec('aboba')

#7
print('7')
newTree.searchPostorderIter(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchPostorderIter('aboba')
#8
print('8')
newTree.searchPostorderRec(89) # ===
print(newTree.root.right) # Проверка к предыдущему
newTree.searchPostorderRec('aboba')