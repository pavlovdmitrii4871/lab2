from deq_stack import Dequeue

numbers = Dequeue()
numbers_2 = Dequeue()

file = 'sifri.txt'
result_file = 'result.txt'
with open(file, 'r') as file, open(result_file, 'w') as result_file:
    for c in file.readlines():
        int_c = int(c)
        if int_c >= 0:
            numbers_2.push_last(int_c)
        else:
            numbers.push_first(int_c)
    for _ in range(len(numbers)):
        num = numbers.pop_last()
        result_file.write(str(num) + '\n')
        print(num)
    for _ in range(len(numbers_2)):
        num = numbers_2.pop_first()
        result_file.write(str(num) + '\n')
        print(num)
