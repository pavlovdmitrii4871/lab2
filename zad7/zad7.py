from deq_stack import Dequeue

# Создаем две пустые очереди (дека)
num1 = Dequeue()  # очередь для отрицательных чисел
num2 = Dequeue()  # очередь для положительных чисел

file = 'isx.txt'
result_file = 'result.txt'

# Открываем файл на чтение и результат на запись
with open(file, 'r') as file, open(result_file, 'w') as result_file:

    # Итерируемся по каждой строке в файле
    for c in file.readlines():
        int_c = int(c)

        # Если число положительное или равно нулю, добавляем его в num2
        if int_c >= 0:
            num2.push_last(int_c)
        # Если число отрицательное, добавляем его в num1
        else:
            num1.push_first(int_c)

    # Печатаем и записываем все отрицательные числа из num1
    for _ in range(len(num1)):
        num = num1.pop_last()
        result_file.write(str(num) + '\n')
        print(num)

    # Печатаем и записываем все положительные числа из num2
    for _ in range(len(num2)):
        num = num2.pop_first()
        result_file.write(str(num) + '\n')
        print(num)
