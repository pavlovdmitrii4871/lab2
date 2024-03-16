from deq_stack import Dequeue

# Создаем две пустые очереди (дека)
numbers = Dequeue()  # очередь для отрицательных чисел
numbers_2 = Dequeue()  # очередь для положительных чисел

file = 'sifri.txt'
result_file = 'result.txt'

# Открываем файл на чтение и результат на запись
with open(file, 'r') as file, open(result_file, 'w') as result_file:

    # Итерируемся по каждой строке в файле
    for c in file.readlines():
        int_c = int(c)

        # Если число положительное или равно нулю, добавляем его в numbers_2
        if int_c >= 0:
            numbers_2.push_last(int_c)
        # Если число отрицательное, добавляем его в numbers
        else:
            numbers.push_first(int_c)

    # Печатаем и записываем все отрицательные числа из numbers
    for _ in range(len(numbers)):
        num = numbers.pop_last()
        result_file.write(str(num) + '\n')
        print(num)

    # Печатаем и записываем все положительные числа из numbers_2
    for _ in range(len(numbers_2)):
        num = numbers_2.pop_first()
        result_file.write(str(num) + '\n')
        print(num)
