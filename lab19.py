class Node:
    def __init__(self, idx):
        self.idx = idx
        self.state = 0  # 0 — не открыта, 1 — открыта, 2 — закрыта
        
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


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

    def kruskal(self):
        if not self.valid:
            print("Краскал: граф задан некорректно")
            return []

        n = len(self.nodes)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                weight = self.adjacency_matrix[i][j]
                if weight != 0: 
                    edges.append((weight, i, j))

        edges.sort() 

        uf = UnionFind(n)
        mst = []
        total_weight = 0

        for weight, u, v in edges:
            if uf.union(u, v):
                mst.append((u, v, weight))
                total_weight += weight
                if len(mst) == n - 1:
                    break

        if len(mst) != n - 1:
            print("Краскал: граф несвязный, остов не существует")
            return []

        print(f"Краскал: найдено остовное дерево весом {total_weight}")
        print(mst)
        return mst

    def prim(self, start_idx=0):
        if not self.valid:
            print("Прим: граф задан некорректно")
            return []

        n = len(self.nodes)
        if start_idx < 0 or start_idx >= n:
            print("Прим: начальная вершина вне диапазона")
            return []

        import heapq

        visited = [False] * n
        min_heap = []  # (вес, из, в)
        mst = []
        total_weight = 0

        visited[start_idx] = True
        for neighbor in range(n):
            weight = self.adjacency_matrix[start_idx][neighbor]
            if weight != 0 and not visited[neighbor]:
                heapq.heappush(min_heap, (weight, start_idx, neighbor))

        while min_heap and len(mst) < n - 1:
            weight, u, v = heapq.heappop(min_heap)
            if visited[v]:
                continue
            visited[v] = True
            mst.append((u, v, weight))
            total_weight += weight
            # Добавляем новые рёбра из v
            for w in range(n):
                next_weight = self.adjacency_matrix[v][w]
                if next_weight != 0 and not visited[w]:
                    heapq.heappush(min_heap, (next_weight, v, w))

        if len(mst) != n - 1:
            print("Прим: граф несвязный, остов не существует")
            return []

        print(f"Прим (старт {start_idx}): найдено остовное дерево весом {total_weight}")
        print(mst)
        return mst
    
matrix = [
    [0, 0, 4, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [4, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

g = Graph(matrix)
g.kruskal()
g.prim()