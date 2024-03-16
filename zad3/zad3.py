# Описание класса Stack
class Stack:
    def init(self):
        self.items = []  # Инициализация пустого списка для хранения элементов стека

    def is_empty(self):
        return len(self.items) == 0  # Проверка, пустой ли стек

    def push(self, item):
        self.items.append(item)  # Добавление элемента в стек

    def pop(self):
        if not self.is_empty():  # Проверка, пустой ли стек
            return self.items.pop()  # Извлечение последнего элемента стека
        return None  # Возвращаем None, если стек пуст

    def peek(self):
        if not self.is_empty():  # Проверка, пустой ли стек
            return self.items[-1]  # Возвращает последний элемент стека
        return None  # Возвращаем None, если стек пуст

    def size(self):
        return len(self.items)  # Возвращает размер стека

    def get_items(self):
        return self.items  # Возвращает все элементы стека


# Функция решения задачи Ханойские башни
def hanoi(n, source, target, auxiliary):
    if n == 1:
        disk = source.pop()
        target.push(disk)  # Переносим диск с одного стека на другой
        return

    hanoi(n-1, source, auxiliary, target)  # Рекурсивный вызов функции с переносом n-1 диска на промежуточный стек

    disk = source.pop()
    target.push(disk)

    hanoi(n-1, auxiliary, target, source)  # Рекурсивный вызов функции с переносом n-1 диска с промежуточного стека на конечный


# Создание трех стеков
tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

# Чтение данных из файла и заполнение стека tower_a
input_filename = 'disks.txt'
output_filename = 'results.txt'
with open(input_filename, "r") as file:
    disks = file.read().split()

for disk in disks:
    tower_a.push(disk)

# Вызов функции hanoi для решения задачи
hanoi(tower_a.size(), tower_a, tower_c, tower_b)

# Запись результатов в файл
with open(output_filename, "w") as file:
    file.write("Стержень A: " + str(tower_a.items) + "\n")  # Запись содержимого стека tower_a в файл
    file.write("Стержень B: " + str(tower_b.items) + "\n")  # Запись содержимого стека tower_b в файл
    file.write("Стержень C: " + str(tower_c.items) + "\n")  # Запись содержимого стека tower_c в файл

# Вывод сообщения о завершении программы
print(f"Результаты записаны в файл {output_filename}.")
