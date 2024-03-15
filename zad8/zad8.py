from deq_stack import Stack


def reverse_file(input_file, output_file):
    stack = []

    # Чтение строк из исходного файла и добавление их в стек
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            stack.append(line)

    # Запись строк в обратном порядке в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        while stack:
            line = stack.pop()
            file.write(line)

    print(f"Файл {input_file} был обработан. Результат записан в файл {output_file}.")


# Пример использования функции
if __name__ == "__main__":
    input_file = "bukvi.txt"  # Путь к исходному файлу
    output_file = "reverse.txt"  # Путь к новому файлу

    reverse_file(input_file, output_file)
