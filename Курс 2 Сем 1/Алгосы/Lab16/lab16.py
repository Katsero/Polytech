class HashTable:
    def __init__(self, size=10, arr=None):
        # Безопасная инициализация массива
        if arr is None:
            arr = []
        
        if size <= 0:
            print("Ошибка: Размер хеш-таблицы должен быть положительным числом.")
            # Создадим минимальную таблицу, чтобы не сломать всё
            size = 1
        self.size = size
        self.table = [[] for _ in range(self.size)]
        
        # Вставка элементов из массива
        for value in arr:
            self.insert(value)

    def _is_number(self, value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def _is_valid_index(self, index):
        return isinstance(index, int) and 0 <= index < self.size

    def _hash(self, value):
        return abs(int(value)) % self.size

    def insert(self, value):
        if not self._is_number(value):
            print(f"Таблица состоит только из чисел")
            return
        index = self._hash(value)
        self.table[index].append(value)

    def search_by_value(self, value):
        if not self._is_number(value):
            print(f"Таблица состоит только из чисел")
            return []
        indices = []
        for i, slot in enumerate(self.table):
            if value in slot:
                indices.append(i)
        return indices

    def search_by_index(self, index):
        if not self._is_valid_index(index):
            print(f"Ошибка: индекс {index} вне диапазона [0, {self.size - 1}].")
            return []
        return self.table[index][:] 

    def pop(self, index):
        if not self._is_valid_index(index):
            print(f"Ошибка: индекс {index} вне диапазона [0, {self.size - 1}]. Удаление пропущено.")
            return []
        removed = self.table[index]
        self.table[index] = []
        return removed

    def remove(self, value):
        if not self._is_number(value):
            print(f"Таблица состоит только из чисел")
            return 0
        count = 0
        for slot in self.table:
            while value in slot:
                slot.remove(value)
                count += 1
        return count

    def output(self):
        for i, slot in enumerate(self.table):
            if slot:
                print(f"Ячейка {i}: {slot}")

newTable = HashTable(14)
newTable.output()
print('--------------')

newTable.insert(4)
newTable.insert(18)
newTable.insert(32)
newTable.insert(5)
newTable.insert(0)
newTable.insert(1)
newTable.output()
print('--------------')

print(newTable.search_by_index(4))
print(newTable.search_by_index(1))
print(newTable.search_by_index(0))
print(newTable.search_by_index(2))
newTable.output()
print('--------------')

print(newTable.search_by_value(18))
print(newTable.search_by_value(4))
print(newTable.search_by_value(0))
print(newTable.search_by_value(6))
newTable.output()
print('--------------')

print(newTable.remove(1))
print(newTable.remove(18))
print(newTable.remove(3))
newTable.output()
print('--------------')

print(newTable.pop(0))
print(newTable.pop(18))
print(newTable.pop(3))
print(newTable.pop(4))
newTable.output()
print('--------------')

newTable.insert('aboba')
newTable.search_by_index(15)
newTable.search_by_index('aboba')
newTable.search_by_value('aboba')
newTable.pop('aboba')
newTable.remove('aboba')
newTable.output()
print('--------------')