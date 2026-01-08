import time
import random

class Pyramide:
    def __init__(self, arr=None, maximal=True):
        self.maximal = maximal
        self.tree = []
        if arr:
            for element in arr:
                self._append_no_log(element)

    def _append_no_log(self, value):
        val = value if self.maximal else -value
        self.tree.append(val)
        idx = len(self.tree)
        while idx > 1:
            parent = idx // 2
            if self.tree[idx - 1] <= self.tree[parent - 1]:
                break
            self.tree[idx - 1], self.tree[parent - 1] = self.tree[parent - 1], self.tree[idx - 1]
            idx = parent

    def pyramideRearrange(self, parentIndex):
        while True:
            largest = parentIndex
            left = parentIndex * 2
            right = parentIndex * 2 + 1

            if left <= len(self.tree) and self.tree[left - 1] > self.tree[largest - 1]:
                largest = left
            if right <= len(self.tree) and self.tree[right - 1] > self.tree[largest - 1]:
                largest = right

            if largest == parentIndex:
                break

            self.tree[parentIndex - 1], self.tree[largest - 1] = self.tree[largest - 1], self.tree[parentIndex - 1]
            parentIndex = largest

    def pyramideSort(self):
        res = []
        while self.tree:
            head = self.tree[0]
            res.append(head if self.maximal else -head)
            last = self.tree.pop()
            if self.tree:
                self.tree[0] = last
                self.pyramideRearrange(1)
        return res


def benchmark_heap():
    print("=== Пирамидальная сортировка (только pyramideSort) ===")
    n = int(input("Число элементов (N): "))
    value_range = int(input("Диапазон значений (0 до RANGE): "))
    iterations = int(input("Число итераций: "))

    # Заготовка: для каждой итерации — свой массив и своя куча (создаются ДО таймера)
    heaps = []
    for _ in range(iterations):
        arr = [random.randint(0, value_range) for _ in range(n)]
        heap = Pyramide(arr, maximal=True)
        heaps.append(heap)

    # Прогрев
    _ = heaps[0].pyramideSort()
    # Восстановим кучу после прогрева (чтобы состояние было как у остальных)
    arr = [random.randint(0, value_range) for _ in range(n)]
    heaps[0] = Pyramide(arr, maximal=True)

    # ЗАМЕР ТОЛЬКО pyramideSort()
    start = time.perf_counter()
    for heap in heaps:
        _ = heap.pyramideSort()
    end = time.perf_counter()

    total_time = end - start
    avg_time = total_time / iterations

    print(f"\n✅ Результаты:")
    print(f"N = {n}, итераций = {iterations}")
    print(f"Общее время: {total_time:.6f} сек")
    print(f"Среднее время на pyramideSort(): {avg_time:.9f} сек")


if __name__ == "__main__":
    benchmark_heap()