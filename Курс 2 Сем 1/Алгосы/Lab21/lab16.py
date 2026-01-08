import time
import random

class HashTable:
    def __init__(self, size=10, arr=None):
        self.size = size if size > 0 else 1
        self.table = [[] for _ in range(self.size)]
        if arr:
            for value in arr:
                self.insert(value)

    def _is_number(self, value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def _hash(self, value):
        return abs(int(value)) % self.size

    def insert(self, value):
        if not self._is_number(value):
            return
        index = self._hash(value)
        self.table[index].append(value)

    def search_by_value(self, value):
        if not self._is_number(value):
            return []
        for slot in self.table:
            if value in slot:
                return [True]
        return []

    def remove(self, value):
        if not self._is_number(value):
            return 0
        count = 0
        for slot in self.table:
            while value in slot:
                slot.remove(value)
                count += 1
        return count


def benchmark_hash():
    print("=== Хеш-таблица Benchmark (время ОПЕРАЦИИ БЕЗ построения) ===")
    n = int(input("Число элементов в таблице (N): "))
    value_range = int(input("Диапазон значений (0 до RANGE): "))
    iterations = int(input("Число итераций: "))

    operations = {
        '1': ('insert', 'Вставка нового элемента'),
        '2': ('search_by_value', 'Поиск существующего элемента'),
        '3': ('remove', 'Удаление существующего элемента'),
    }

    print("\nВыберите операцию:")
    for key, (_, name) in operations.items():
        print(f"{key}. {name}")
    choice = input("Номер операции: ")
    if choice not in operations:
        print("Неверный выбор!")
        return

    op_name, op_desc = operations[choice]

    # Генерация данных ДО замера
    test_cases = []
    for _ in range(iterations):
        values = random.sample(range(value_range), min(n, value_range))
        if op_name == 'insert':
            new_val = random.randint(value_range, value_range * 2)
            test_cases.append((values, new_val))
        else:
            target = random.choice(values)
            test_cases.append((values, target))

    # Создание всех таблиц ДО таймера
    tables_and_args = []
    for values, arg in test_cases:
        ht = HashTable(size=len(values) or 1, arr=values)
        tables_and_args.append((ht, arg))

    # Прогрев
    first_ht, first_arg = tables_and_args[0]
    getattr(first_ht, op_name)(first_arg)

    # ЗАМЕР ТОЛЬКО ОПЕРАЦИЙ
    start = time.perf_counter()
    for ht, arg in tables_and_args:
        getattr(ht, op_name)(arg)
    end = time.perf_counter()

    total_time = end - start
    avg_time = total_time / iterations

    print(f"\n✅ Результаты:")
    print(f"Операция: {op_desc}")
    print(f"Размер таблицы: {n}, итераций: {iterations}")
    print(f"Общее время: {total_time:.6f} сек")
    print(f"Среднее время на операцию: {avg_time:.9f} сек")
    print("💡 Примечание: Время создания таблицы НЕ включено в замер.")


if __name__ == "__main__":
    benchmark_hash()