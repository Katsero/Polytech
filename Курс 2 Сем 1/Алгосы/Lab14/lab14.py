import sys

class Node:
    def __init__(self, key, color='red', left=None, right=None, parent=None):
        self.key = key
        self.color = color  # 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node({self.key}, {self.color})"

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='black')  # Sentinel leaf node
        self.head = self.NIL

    ## ERRORS
    def tie(self):
        print(f'Tree is empty')
        return

    def insert(self, key):
        new_node = Node(key, 'red', self.NIL, self.NIL)
        if self.head == self.NIL:
            self.head = new_node
            new_node.color = 'black'
            return

        # Найти место для вставки
        current = self.head
        parent = None
        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Балансировка
        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Case 1: uncle is red -> recolor
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: node is right child -> left rotate
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: node is left child -> right rotate
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Case 1: uncle is red -> recolor
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: node is left child -> right rotate
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: node is right child -> left rotate
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)

        self.head.color = 'black'

    def delete(self, key):
        node = self._search(key)
        if node == self.NIL:
            print(f"Key {key} not found.")
            return

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 'black':
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.head and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    # Case 1
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    # Case 2
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        # Case 3
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.head
            else:
                w = x.parent.left
                if w.color == 'red':
                    # Case 1
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    # Case 2
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        # Case 3
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.head
        x.color = 'black'

    def _search(self, key):
        current = self.head
        while current != self.NIL:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return self.NIL

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent == None:
            self.head = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
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
        if x.parent == None:
            self.head = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    ## Output (obviously)
    def output(self, node=None, depth=0, is_root=True):
        if is_root:
            if self.head == self.NIL:
                self.tie()
                return
            print('tree:')

        current = self.head if node is None else node

        if current == self.NIL:
            return

        # право
        self.output(current.right, depth + 1, False)

        # центр
        if current.color == 'red':
            print('    ' * depth + f"\033[31m{current.key}\033[0m")
        else:
            print('    ' * depth + str(current.key))

        # лево
        self.output(current.left, depth + 1, False)

        if is_root:
            print('-------')

# --- Дополнительно: функция для создания несбалансированного дерева ---
def build_unbalanced_tree(tree, keys):
    """Вставляет ключи последовательно, создавая несбалансированное дерево"""
    for key in keys:
        tree.insert(key)
        print(f"\n--- После вставки {key} ---")
        tree.output()

# --- Пример использования ---
if __name__ == "__main__":
    rbt = RedBlackTree()

    print("=== Создание несбалансированного дерева ===")
    unbalanced_keys = [10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]
    build_unbalanced_tree(rbt, unbalanced_keys)

    print("\n=== Вставка нового элемента (например, 9) ===")
    rbt.insert(9)
    rbt.output()

    print("\n=== Удаление элемента (например, 10) ===")
    rbt.delete(10)
    rbt.output()

    print("\n=== Удаление ещё одного (например, 15) ===")
    rbt.delete(15)
    rbt.output()