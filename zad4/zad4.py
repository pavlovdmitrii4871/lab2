# Импортируем класс Stack из файла deq_stack.py
from deq_stack import Stack

# Функция check_brackets принимает два аргумента: имя входного файла и имя выходного файла
def check_brackets(filename, output_filename):
    stack = Stack()  # инициализация стека
    
    # Открываем входной файл в режиме чтения с использованием кодировки utf-8
    with open(filename, 'r', encoding='utf-8') as file:
        # Построчно читаем файл
        for line in file:
            # Перебираем каждый символ в строке
            for char in line:
                if char == '(':  # Если символ - открывающая скобка
                    stack.push(char)  # добавляем открывающую скобку в стек
                elif char == ')':  # Если символ - закрывающая скобка
                    if not len(stack):  # если стек пуст, то скобка несбалансирована
                        # Если стек пуст, это означает, что встретилась закрывающая скобка без предшествующей открывающей скобки
                        return False
                    stack.pop()  # Иначе удаляем последнюю открывающую скобку из стека

    # Проверяем, все ли открывающие скобки были закрыты
    balanced = len(stack) == 0  # Если стек пуст, то все скобки сбалансированы

    # Открываем выходной файл в режиме записи с использованием кодировки utf-8
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        if balanced:
            output_file.write("Скобки сбалансированы")
        else:
            output_file.write("Скобки несбалансированы")

    return balanced


filename = 'isx.txt'  # имя текстового файла с программой
output_filename = 'result.txt'  # имя файла для записи результата

# Вызываем функцию check_brackets с указанными именами файлов и сохраняем результат в переменную result
result = check_brackets(filename, output_filename)

# Выводим результат в зависимости от значения переменной result
if result:
    print("Скобки сбалансированы")
else:
    print("Скобки несбалансированы")
