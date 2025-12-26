class Graph:
    def __init__(self, adjacency_matrix):
        self.valid = True
        self.adjacency_matrix = []

        if not adjacency_matrix:
            self.valid = False
            return

        n = len(adjacency_matrix)
        if not all(len(row) == n for row in adjacency_matrix):
            self.valid = False
            return

        for i in range(n):
            for j in range(n):
                val = adjacency_matrix[i][j]
                if not isinstance(val, (int, float)) or val < 0:
                    self.valid = False
                    return

        self.adjacency_matrix = [list(row) for row in adjacency_matrix]
        self.n = n

    def dejkstra(self, start, end):
        if not self.valid:
            print("Дейкстра: Граф задан некорректно (матрица не квадратная, пустая или содержит отрицательные веса)")
            return

        if not (0 <= start < self.n and 0 <= end < self.n):
            print("Дейкстра: Начальная или конечная вершина вне диапазона")
            return

        dist = [float('inf')] * self.n
        prev = [None] * self.n
        used = [False] * self.n
        dist[start] = 0

        for _ in range(self.n):
            min_dist = float('inf')
            u = -1
            for i in range(self.n):
                if not used[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1:
                break
            used[u] = True

            for v in range(self.n):
                w = self.adjacency_matrix[u][v]
                if w == 0:
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

        if dist[end] == float('inf'):
            print(f"Путь от {start} до {end} не существует")
        else:
            path = []
            cur = end
            while cur is not None:
                path.append(cur)
                cur = prev[cur]
            path.reverse()
            print(f"Кратчайший путь от {start} до {end}: {' -> '.join(map(str, path))}")
            print(f"Вес пути: {dist[end]}")

matrix = [
    [0, 0, 4, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [4, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

g1 = Graph(matrix)
g1.dejkstra(0, 5)

# print("-------------")

# g2 = Graph([])
# g2.dejkstra(0, 1)

# print("-------------")

# g3 = Graph([[1, 0], []])
# g3.dejkstra(0, 1)