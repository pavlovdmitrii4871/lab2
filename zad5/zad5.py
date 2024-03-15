from deq_stack import Dequeue


def check_brackets(filename):
    deque_skobka = Dequeue()  # инициализация стека
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char == '[':
                    deque_skobka.push_last(char)  # добавляем открывающую скобку в стек
                elif char == ']':
                    if not deque_skobka:  # если стек пуст, то скобка несбалансирована
                        return False
                    else:
                        deque_skobka.pop_last()  # удаляем пару открывающей скобки из стека

    return len(deque_skobka) == 0  # если стек пуст, то все скобки сбалансированы


filename = 'alg2.txt'  # имя текстового файла с программой
output_filename = 'brackets_balance_result.txt'
result = check_brackets(filename)
if result:
    print("Скобки сбалансированы")
else:
    print("Скобки несбалансированы")

# Открытие файла для записи
with open(output_filename, 'w', encoding='utf-8') as output_file:
    if result:
        output_file.write("Скобки сбалансированы")
    else:
        output_file.write("Скобки несбалансированы")

