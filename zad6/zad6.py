from deq_stack import Stack

numbers = Stack()
chars = Stack()
symbols = Stack()

file = 'symbol.txt'
result_file = 'results.txt'  # имя файла для записи результата

with open(file, 'r') as file:
    for c in file.read():
        if c.isdigit():
            numbers.push(c)
        elif c.isalpha():
            chars.push(c)
        else:
            symbols.push(c)

with open(result_file, 'w') as f:  # открываем файл для записи
    f.write("Numbers:\n")
    for _ in range(0, len(numbers)):
        num = numbers.pop()
        f.write(num + "\n")  # записываем число в файл
        print(num)  # выводим число в консоль

    f.write("\nChars:\n")
    for _ in range(0, len(chars)):
        char = chars.pop()
        f.write(char + "\n")  # записываем букву в файл
        print(char)  # выводим букву в консоль

    f.write("\nSymbols:\n")
    for _ in range(0, len(symbols)):
        symbol = symbols.pop()
        f.write(symbol + "\n")  # записываем символ в файл
        print(symbol)  # выводим символ в консоль

print("Результат записан в файл 'results.txt'.")
