# Импорт модуля Stack из файла deq_stack.py для использования стека
from deq_stack import Stack

# Определение функции reverse_file, которая принимает путь к исходному файлу и путь к новому файлу
def reverse_file(input_file, output_file):
    stack = []  # Создание пустого стека для хранения строк

    # Чтение строк из исходного файла и добавление их в стек
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            stack.append(line)  # Добавление строки в стек

    # Запись строк в обратном порядке в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        while stack:  # Пока стек не пустой
            line = stack.pop()  # Извлечение последней строки из стека
            file.write(line)  # Запись строки в новый файл

    # Вывод сообщения о завершении обработки файлов
    print(f"Файл {input_file} обработан. Результат записан в файл {output_file}.")


# Пример использования функции
if name == "main":  # Если код выполняется как самостоятельный файл
    input_file = "isx.txt"  # Путь к исходному файлу
    output_file = "res.txt"  # Путь к новому файлу

    reverse_file(input_file, output_file)  # Вызов функции reverse_file для обработки файлов
