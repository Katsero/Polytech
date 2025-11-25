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

    def treeAppend(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while current:
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

    def treeOutput(self, node = None, depth = 0, res=[]):
        if depth == 0:
            node = self.root

        if not res[depth]:
            res[depth] = []

        if node:
            res[depth].append(node.value)
            res = self.treeOutput(node.left,depth,res)
            res = self.treeOutput(node.right,depth,res)
        
        if depth == 0:
            print(res)
        else:
            return(res)
    # def treeOutput(self, node=None, depth=0):
    #     if depth == 0:
    #         node = self.root

    #     if node:
    #         print("  "*depth, node.value)
    #         self.treeOutput(node.right, depth+1)
    #         self.treeOutput(node.left, depth+1)

newTree = Tree([23, 87, 5, 64, 91, 12, 76, 34, 45, 89])
print('created')
print('tree:')
newTree.treeOutput()
