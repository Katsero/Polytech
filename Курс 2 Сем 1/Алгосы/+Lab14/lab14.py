import sys

class Node:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node({self.value}, {self.color})"

class RedBlackTree:
    def __init__(self, values=None):
        self.NIL = Node(None, color='black')
        self.head = self.NIL

        if values is not None:
            print("Изначальное дерево:")
            for v in values:
                self._insert_unbalanced(v)
            self.output()
            print("\nБалансировка (структура → раскраска по уровням):")
            self.balance_to_min_height_and_color_by_level()
            self.output()

    def _insert_unbalanced(self, value):
        if self.head == self.NIL:
            self.head = Node(value, 'black', self.NIL, self.NIL)
            return

        current = self.head
        while True:
            if value < current.value:
                if current.left == self.NIL:
                    current.left = Node(value, 'red', self.NIL, self.NIL, current)
                    break
                else:
                    current = current.left
            else:
                if current.right == self.NIL:
                    current.right = Node(value, 'red', self.NIL, self.NIL, current)
                    break
                else:
                    current = current.right

    def balance_to_min_height_and_color_by_level(self):
        """Сбалансировать структуру до минимальной высоты и раскрасить: полные уровни — чёрные, последний — красные."""
        if self.head == self.NIL:
            return

        nodes = []
        self._inorder_collect_nodes(self.head, nodes)

        self.head = self._build_balanced_from_nodes(nodes, 0, len(nodes) - 1)
        if self.head != self.NIL:
            self.head.parent = None

        max_depth = self._find_max_depth(self.head)

        self._color_by_max_depth(self.head, 0, max_depth)
        self.head.color = 'black'

    def _inorder_collect_nodes(self, node, acc):
        if node == self.NIL:
            return
        self._inorder_collect_nodes(node.left, acc)
        acc.append(node)
        self._inorder_collect_nodes(node.right, acc)

    def _build_balanced_from_nodes(self, nodes, start, end):
        if start > end:
            return self.NIL
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self._build_balanced_from_nodes(nodes, start, mid - 1)
        root.right = self._build_balanced_from_nodes(nodes, mid + 1, end)
        if root.left != self.NIL:
            root.left.parent = root
        if root.right != self.NIL:
            root.right.parent = root
        return root

    def _find_max_depth(self, node, depth=0):
        if node == self.NIL:
            return depth - 1
        left_depth = self._find_max_depth(node.left, depth + 1)
        right_depth = self._find_max_depth(node.right, depth + 1)
        return max(left_depth, right_depth)

    def _color_by_max_depth(self, node, current_depth, max_depth):
        if node == self.NIL:
            return
        if current_depth < max_depth:
            node.color = 'black'
        else:
            node.color = 'red'
        self._color_by_max_depth(node.left, current_depth + 1, max_depth)
        self._color_by_max_depth(node.right, current_depth + 1, max_depth)

    def output(self, node=None, depth=0, is_root=True):
        if is_root:
            if self.head == self.NIL:
                print('Tree is empty')
                return
            print('tree:')

        current = self.head if node is None else node

        if current == self.NIL:
            return

        self.output(current.right, depth + 1, False)

        if current.color == 'red':
            print('    ' * depth + f"\033[31m{current.value}\033[0m")
        else:
            print('    ' * depth + str(current.value))

        self.output(current.left, depth + 1, False)

        if is_root:
            print('-------')

    def insert(self, value):
        new_node = Node(value, 'red', self.NIL, self.NIL)
        if self.head == self.NIL:
            self.head = new_node
            new_node.color = 'black'
            return

        current = self.head
        parent = None
        while current != self.NIL:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.insertFix(new_node)

    def insertFix(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)

        self.head.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.head = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.head = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


# ТЕСТ
if __name__ == "__main__":
    values = [10, 20, 30, 40]
    print(">>> NewTree = RedBlackTree([10,20,30,40])")
    rbt = RedBlackTree(values)