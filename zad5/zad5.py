# Импортируем модуль Dequeue из файла deq_stack.py, который содержит реализацию дека (двусторонней очереди)
from deq_stack import Dequeue
# Функция check_brackets принимает в качестве аргумента имя текстового файла
def check_brackets(filename):
    # Инициализация дека для хранения скобок
    deque_skobka = Dequeue()
    # Открытие файла на чтение
    with open(filename, 'r', encoding='utf-8') as file:
        # Читаем файл построчно
        for line in file:
            # Итерация по каждому символу в строке
            for char in line:
                # Если символ - открывающая скобка '['
                if char == '[':
                    # Добавляем открывающую скобку в дек
                    deque_skobka.push_last(char)
                # Если символ - закрывающая скобка ']'
                elif char == ']':
                    # Если дек пустой, то скобка несбалансирована
                    if not deque_skobka:
                        return False
                    else:
                        # Иначе, удаляем пару открывающей скобки из дека
                        deque_skobka.pop_last()
    
    # Если после обработки файла дек оказался пустым, то все скобки сбалансированы
    return len(deque_skobka) == 0
# Имя текстового файла с программой
filename = 'isx.txt'
# Имя файла для записи результатов
output_filename = 'result.txt'
# Проверяем баланс скобок в файле
result = check_brackets(filename)
# Если результат - True, то скобки сбалансированы, иначе - несбалансированы
if result:
    print("Скобки сбалансированы")
else:
    print("Скобки несбалансированы")
# Открываем файл на запись
with open(output_filename, 'w', encoding='utf-8') as output_file:
    # Если результат - True, записываем "Скобки сбалансированы" в файл, иначе - "Скобки несбалансированы"
    if result:
        output_file.write("Скобки сбалансированы")
    else:
        output_file.write("Скобки несбалансированы")
