# Импортирование класса Stack из файла deq_stack.py
from deq_stack import Stack

# Создание трех стеков для цифр, букв и символов
numbers = Stack()
chars = Stack()
symbols = Stack()

# Имя файла с символами
file = 'symbol.txt'
# Имя файла для записи результата
result_file = 'results.txt'

# Открытие файла в режиме чтения
with open(file, 'r') as file:
    # Чтение каждого символа из файла
    for c in file.read():
        # Если символ является цифрой, добавить его в стек numbers
        if c.isdigit():
            numbers.push(c)
        # Если символ является буквой, добавить его в стек chars
        elif c.isalpha():
            chars.push(c)
        # Если символ не является ни цифрой, ни буквой, добавить его в стек symbols
        else:
            symbols.push(c)

# Открытие файла в режиме записи
with open(result_file, 'w') as f:
    f.write("Numbers:\n")
    # Печать всех цифр из стека numbers в файл
    for _ in range(0, len(numbers)):
        num = numbers.pop()
        f.write(num + "\n")
        print(num)

    f.write("\nChars:\n")
    # Печать всех букв из стека chars в файл
    for _ in range(0, len(chars)):
        char = chars.pop()
        f.write(char + "\n")
        print(char)

    f.write("\nSymbols:\n")
    # Печать всех символов из стека symbols в файл
    for _ in range(0, len(symbols)):
        symbol = symbols.pop()
        f.write(symbol + "\n")
        print(symbol)

# Вывод сообщения после завершения программы
print("Результат записан в файл 'results.txt'.")
