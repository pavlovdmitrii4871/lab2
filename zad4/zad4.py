from deq_stack import Stack

def check_brackets(filename, output_filename):
    stack = Stack()  # инициализация стека
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char == '(':
                    stack.push(char)  # добавляем открывающую скобку в стек
                elif char == ')':
                    if not len(stack):  # если стек пуст, то скобка несбалансирована
                        return False
                    stack.pop()

    balanced = len(stack) == 0  # если стек пуст, то все скобки сбалансированы

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        if balanced:
            output_file.write("Скобки сбалансированы")
        else:
            output_file.write("Скобки несбалансированы")

    return balanced

filename = 'alg.txt'  # имя текстового файла с программой
output_filename = 'brackets_balance_result.txt'  # имя файла для записи результата
result = check_brackets(filename, output_filename)
if result:
    print("Скобки сбалансированы")
else:
    print("Скобки несбалансированы")
