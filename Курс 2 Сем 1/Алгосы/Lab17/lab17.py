class Node:
    def __init__(self, idx):
        self.idx = idx
        self.state = 0  # 0 — не открыта, 1 — открыта, 2 — закрыта


class Graph:
    def __init__(self, adjacency_matrix):
        self.valid = True
        self.nodes = []
        self.adjacency_matrix = []

        if not adjacency_matrix:
            self.valid = False
            return

        n = len(adjacency_matrix)
        if not all(len(row) == n for row in adjacency_matrix):
            self.valid = False
            return

        self.nodes = [Node(i) for i in range(n)]
        self.adjacency_matrix = [list(row) for row in adjacency_matrix]

    def reset_states(self):
        for node in self.nodes:
            node.state = 0

    def bfs(self, start_idx):
        if not self.valid:
            print("BFS: Граф задан некорректно (матрица не квадратная или пустая)")
            return []

        if start_idx < 0 or start_idx >= len(self.nodes):
            print("BFS: Начальная вершина указана неверно — граф не содержит такой вершины")
            return []

        self.reset_states()
        result = []
        queue = [start_idx]
        self.nodes[start_idx].state = 1

        while queue:
            cur = queue.pop(0)
            self.nodes[cur].state = 2
            result.append(cur)
            for neighbor, connected in enumerate(self.adjacency_matrix[cur]):
                if connected and self.nodes[neighbor].state == 0:
                    self.nodes[neighbor].state = 1
                    queue.append(neighbor)

        self._check_and_reset(result, "BFS")
        return result

    def dfs(self, start_idx):
        if not self.valid:
            print("DFS: Граф задан некорректно (матрица не квадратная или пустая)")
            return []

        if start_idx < 0 or start_idx >= len(self.nodes):
            print("DFS: Начальная вершина указана неверно — граф не содержит такой вершины")
            return []

        self.reset_states()
        result = []
        stack = [start_idx]

        while stack:
            cur = stack.pop()
            if self.nodes[cur].state == 0:
                self.nodes[cur].state = 2
                result.append(cur)
                neighbors = [
                    i for i, connected in enumerate(self.adjacency_matrix[cur])
                    if connected and self.nodes[i].state == 0
                ]
                for neighbor in reversed(neighbors):
                    stack.append(neighbor)

        self._check_and_reset(result, "DFS")
        return result

    def _check_and_reset(self, result, method_name):
        all_closed = all(node.state == 2 for node in self.nodes)
        if all_closed:
            print(f"{method_name}: все вершины посещены.\n{result}")
        else:
            print(f"{method_name}: не все вершины посещены!\n{result}")
        self.reset_states()


matrix = [
    [0, 0, 4, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [4, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

g = Graph(matrix)
g.bfs(0)
g.dfs(0)