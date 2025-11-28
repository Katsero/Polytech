class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Pyramide():
    def __init__(self, arr = None):
        self.root = None
        for elem in arr:
            self.pyramideAppend(elem)

    def pyramideAppend(self, value):
        if not self.root:
            self.root = Node(value)
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = Node(value)
                break
            if not current.right:
                current.right = Node(value)
                break

            queue.append(current.left)
            queue.append(current.right)

        self.pyramideRearrange()

    def pyramideRearrange(self, starting = True):
        pass

        

    def output(self, node=None, depth=0):
        if depth == 0:
            print('tree:')
            node = self.root

        if node:
            print("  "*depth, node.value)
            self.treeOutput(node.right, depth+1)
            self.treeOutput(node.left, depth+1)
        
        if depth == 0:
            print('-------')

        
