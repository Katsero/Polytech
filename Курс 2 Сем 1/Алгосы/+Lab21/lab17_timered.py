import time
import random

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.state = 0

class Graph:
    def __init__(self, adjacency_matrix):
        n = len(adjacency_matrix)
        self.nodes = [Node(i) for i in range(n)]
        self.adjacency_matrix = [list(row) for row in adjacency_matrix]

    def reset_states(self):
        for node in self.nodes:
            node.state = 0

    def bfs(self, start_idx):
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
        return result

    def dfs(self, start_idx):
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
        return result


def generate_sparse_graph(n, density=0.1):
    matrix = [[0] * n for _ in range(n)]
    max_edges = int(n * (n - 1) * density / 2)
    edges = 0
    attempts = 0
    while edges < max_edges and attempts < max_edges * 10:
        i, j = random.sample(range(n), 2)
        if matrix[i][j] == 0:
            w = random.randint(1, 10)
            matrix[i][j] = w
            matrix[j][i] = w
            edges += 1
        attempts += 1
    return matrix


def benchmark_graph():
    print("=== Обход графа (BFS/DFS) Benchmark ===")
    n = int(input("Число вершин (N): "))
    iterations = int(input("Число итераций: "))

    density = 0.1

    operations = {
        '1': ('bfs', 'Обход в ширину (BFS)'),
        '2': ('dfs', 'Обход в глубину (DFS)'),
    }

    print("\nВыберите операцию:")
    for key, (_, name) in operations.items():
        print(f"{key}. {name}")
    choice = input("Номер операции: ")
    if choice not in operations:
        print("Неверный выбор!")
        return

    op_name, op_desc = operations[choice]

    test_cases = []
    for _ in range(iterations):
        adj_mat = generate_sparse_graph(n, density)
        g = Graph(adj_mat)
        start = random.randint(0, n - 1)
        test_cases.append((g, start))

    g0, s0 = test_cases[0]
    getattr(g0, op_name)(s0)

    start_time = time.perf_counter()
    for graph, start in test_cases:
        _ = getattr(graph, op_name)(start)
    end_time = time.perf_counter()

    total = end_time - start_time
    avg = total / iterations

    print(f"\nРезультаты:")
    print(f"Операция: {op_desc}")
    print(f"N = {n}, плотность = {density:.1%} (фиксирована), итераций = {iterations}")
    print(f"Общее время: {total:.6f} сек")
    print(f"Среднее время на операцию: {avg:.9f} сек")


if __name__ == "__main__":
    benchmark_graph()