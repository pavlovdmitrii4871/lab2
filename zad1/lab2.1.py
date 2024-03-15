from deq_stack import Dequeue


def pop_min(deq):
    min_element = deq.pop_first()
    l = len(deq)
    deq.push_last(min_element)
    for _ in range(0, l):
        el = deq.pop_first()
        min_element = min(el, min_element)
        deq.push_last(el)
    for _ in range(0, len(deq)):
        el = deq.pop_first()
        if el != min_element:
            deq.push_last(el)
    return min_element


def sort_books(books):
    deq = Dequeue()
    sort_deq = Dequeue()
    for book in books:
        deq.push_last(book.strip())
    while len(deq):
        sort_deq.push_first(pop_min(deq))
    return sort_deq


# Укажите путь к файлу с названиями книг
input_file_path = "books.txt"
output_file_path = "sorted_books.txt"

books = []

# Открытие файла и чтение содержимого
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        books.append(line)

sorted_books = sort_books(books)

# Вывод отсортированных названий книг
print("Отсортированные названия книг:")
for _ in range(0, len(sorted_books)):
    book = sorted_books.pop_last()
    print(book)

# Запись отсортированных названий книг в отдельный файл
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for book in sorted(books):
        output_file.write(book)
print("Результаты записаны в файл:", output_file_path)
