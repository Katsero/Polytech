import time
import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            for elem in arr:
                self.treeAppend(elem)

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
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    return
                current = current.right

    def treeRemove(self, value):
        if not self.root:
            return
        if self.root.value == value:
            if not self.root.left or not self.root.right:
                self.root = self.root.left if self.root.left else self.root.right
                return
            current = self.root.right
            if not current.left:
                self.root, current.left = current, self.root.left
                return
            while current.left.left:
                current = current.left
            current.left.left, current.left.right, current.left, self.root = \
                self.root.left, self.root.right, current.left.right, current.left
            return

        current = self.root
        while current:
            if value < current.value:
                if current.left and current.left.value == value:
                    if not current.left.left or not current.left.right:
                        current.left = current.left.left if current.left.left else current.left.right
                        return
                    minimal = current.left.right
                    if not minimal.left:
                        current.left, minimal.left = minimal, current.left.left
                        return
                    while minimal.left.left:
                        minimal = minimal.left
                    minimal.left.left, minimal.left.right, minimal.left, current.left = \
                        current.left.left, current.left.right, minimal.left.right, minimal.left
                    return
                current = current.left
            elif value > current.value:
                if current.right and current.right.value == value:
                    if not current.right.left or not current.right.right:
                        current.right = current.right.left if current.right.left else current.right.right
                        return
                    minimal = current.right.right
                    if not minimal.left:
                        current.right, minimal.left = minimal, current.right.left
                        return
                    while minimal.left.left:
                        minimal = minimal.left
                    minimal.left.left, minimal.left.right, minimal.left, current.right = \
                        current.right.left, current.right.right, minimal.left.right, minimal.left
                    return
                current = current.right

    def searchWidthIter(self, value):
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    def searchWidthRec(self, value, queue=None, depth=0):
        if not self.root:
            return None
        if depth == 0:
            queue = [self.root]
        newqueue = []
        for node in queue:
            if node.value == value:
                return node
            if node.left:
                newqueue.append(node.left)
            if node.right:
                newqueue.append(node.right)
        if newqueue:
            return self.searchWidthRec(value, newqueue, depth + 1)
        return None

    def searchPreorderIter(self, value):
        if not self.root:
            return None
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current.value == value:
                return current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return None

    def searchPreorderRec(self, value, current=None, depth=0):
        if depth == 0:
            current = self.root
        if current is None:
            return None
        if current.value == value:
            return current
        if current.left:
            res = self.searchPreorderRec(value, current.left, depth + 1)
            if res:
                return res
        if current.right:
            res = self.searchPreorderRec(value, current.right, depth + 1)
            return res
        return None

    def searchInorderIter(self, value):
        if not self.root:
            return None
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.value == value:
                return current
            current = current.right
        return None

    def searchInorderRec(self, value, current=None, depth=0):
        if depth == 0:
            current = self.root
        if current is None:
            return None
        if current.left:
            res = self.searchInorderRec(value, current.left, depth + 1)
            if res:
                return res
        if current.value == value:
            return current
        if current.right:
            res = self.searchInorderRec(value, current.right, depth + 1)
            return res
        return None

    def searchPostorderIter(self, value):
        if not self.root:
            return None
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
                return current
        return None

    def searchPostorderRec(self, value, current=None, depth=0):
        if depth == 0:
            current = self.root
        if current is None:
            return None
        if current.left:
            res = self.searchPostorderRec(value, current.left, depth + 1)
            if res:
                return res
        if current.right:
            res = self.searchPostorderRec(value, current.right, depth + 1)
            if res:
                return res
        if current.value == value:
            return current
        return None

    def _collect_values(self):
        """Итеративный сбор всех значений (preorder)"""
        if not self.root:
            return []
        values = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            values.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return values


def benchmark_bst():
    print("=== BST Benchmark (время операции БЕЗ построения дерева) ===")
    n = int(input("Число элементов в дереве (N): "))
    value_range = int(input("Диапазон значений (0 до RANGE): "))
    iterations = int(input("Число итераций: "))

    operations = {
        '1': ('searchWidthIter', 'Поиск в ширину (итеративный)'),
        '2': ('searchWidthRec', 'Поиск в ширину (рекурсивный)'),
        '3': ('searchPreorderIter', 'Preorder (итеративный)'),
        '4': ('searchPreorderRec', 'Preorder (рекурсивный)'),
        '5': ('searchInorderIter', 'Inorder (итеративный)'),
        '6': ('searchInorderRec', 'Inorder (рекурсивный)'),
        '7': ('searchPostorderIter', 'Postorder (итеративный)'),
        '8': ('searchPostorderRec', 'Postorder (рекурсивный)'),
        '9': ('treeAppend', 'Вставка нового элемента'),
        '10': ('treeRemove', 'Удаление существующего элемента'),
    }

    print("\nВыберите операцию:")
    for key, (_, name) in operations.items():
        print(f"{key}. {name}")
    choice = input("Номер операции: ")
    if choice not in operations:
        print("Неверный выбор!")
        return

    op_name, op_desc = operations[choice]

    # Убедимся, что диапазон достаточен для уникальных значений
    actual_range = max(value_range, n * 10)
    values = random.sample(range(actual_range), n)  # всегда уникальные
    tree = Tree(values)  # ← создание ВНЕ таймера
    all_values = values  # исходные значения (уникальны)

    # === Генерация списка аргументов ДО замера ===
    args = []
    if op_name == 'treeAppend':
        # Генерируем `iterations` новых уникальных значений
        used_set = set(all_values)
        for _ in range(iterations):
            while True:
                candidate = random.randint(actual_range, actual_range * 2)
                if candidate not in used_set:
                    args.append(candidate)
                    used_set.add(candidate)  # избегаем дубликатов между вставками
                    break
    else:
        # Для поиска/удаления — случайные значения из дерева
        for _ in range(iterations):
            args.append(random.choice(all_values))

    method = getattr(tree, op_name)

    # Прогрев
    _ = method(args[0])

    # === ЗАМЕР ТОЛЬКО ОПЕРАЦИЙ ===
    start = time.perf_counter()
    for arg in args:
        if op_name == 'treeAppend':
            tree.treeAppend(arg)
            tree.treeRemove(arg)  # восстанавливаем исходное дерево
        else:
            _ = method(arg)
    end = time.perf_counter()

    total_time = end - start
    avg_time = total_time / iterations

    print(f"\nРезультаты:")
    print(f"Операция: {op_desc}")
    print(f"Размер дерева: {n}, итераций: {iterations}")
    print(f"Общее время: {total_time:.6f} сек")
    print(f"Среднее время на операцию: {avg_time:.9f} сек")
    print("Примечание: Время создания дерева НЕ включено в замер.")


if __name__ == "__main__":
    benchmark_bst()