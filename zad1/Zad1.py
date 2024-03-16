# Импортируем модуль "Dequeue" из файла "deq_stack.py"
from deq_stack import Dequeue

# Функция для извлечения наименьшего элемента из дека
def pop_min(deq):
    # Извлекаем первый элемент из дека
    min_element = deq.pop_first()
    # Получаем длину дека
    l = len(deq)
    # Возвращаем наименьший элемент в дек
    deq.push_last(min_element)
    
    # Перебираем все элементы в деке
    for _ in range(0, l):
        # Извлекаем первый элемент из дека
        el = deq.pop_first()
        # Сравниваем текущий элемент и наименьший элемент
        min_element = min(el, min_element)
        # Возвращаем элемент обратно в дек
        deq.push_last(el)
    
    # Перебираем все элементы в деке
    for _ in range(0, len(deq)):
        # Извлекаем первый элемент из дека
        el = deq.pop_first()
        # Если элемент не является наименьшим элементом, возвращаем его обратно в дек
        if el != min_element:
            deq.push_last(el)
    
    # Возвращаем наименьший элемент
    return min_element

# Функция для сортировки книг
def sort_books(books):
    # Создаем два дека: deq и sort_deq
    deq = Dequeue()
    sort_deq = Dequeue()
    
    # Перебираем все книги
    for book in books:
        # Удаляем лишние пробелы в начале и конце строки
        deq.push_last(book.strip())
    
    # Пока в деке есть элементы, извлекаем наименьший элемент и добавляем его в sort_deq
    while len(deq):
        sort_deq.push_first(pop_min(deq))
    
    # Возвращаем отсортированный дек с названиями книг
    return sort_deq

# Указываем путь к входному и выходному файлам
input_file_path = "isx.txt"
output_file_path = "res.txt"

# Создаем пустой список для хранения названий книг
books = []

# Открываем файл и считываем его содержимое
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Добавляем каждую строку в список книг
        books.append(line)

# Сортируем книги
sorted_books = sort_books(books)

# Выводим отсортированные названия книг на экран
print("Отсортированные названия книг:")
for _ in range(0, len(sorted_books)):
    book = sorted_books.pop_last()
    print(book)

# Записываем отсортированные названия книг в отдельный файл
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for book in sorted(books):
        output_file.write(book)

# Выводим сообщение о завершении программы и указываем путь к выходному файлу
print("Результаты записаны в файл:", output_file_path)
