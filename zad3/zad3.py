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
stackl_a = Stack()
stackl_b = Stack()
stackl_c = Stack()

# Чтение данных из файла и заполнение стека stackl_a
input_filename = 'disks.txt'
output_filename = 'res.txt'
with open(input_filename, "r") as file:
    disks = file.read().split()

for disk in disks:
    stackl_a.push(disk)

# Вызов функции hanoi для решения задачи
hanoi(stackl_a.size(), stackl_a, stackl_c, stackl_b)

# Запись результатов в файл
with open(output_filename, "w") as file:
    file.write("Стержень A: " + str(stackl_a.items) + "\n")  # Запись содержимого стека stackl_a в файл
    file.write("Стержень B: " + str(stackl_b.items) + "\n")  # Запись содержимого стека stackl_b в файл
    file.write("Стержень C: " + str(stackl_c.items) + "\n")  # Запись содержимого стека stackl_c в файл

# Вывод сообщения о завершении программы
print(f"Результаты записаны в файл {output_filename}.")
