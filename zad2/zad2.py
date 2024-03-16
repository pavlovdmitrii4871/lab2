# Импортируем класс Dequeue из модуля deq_stack
from deq_stack import Dequeue

# Функция для расшифровки сообщения
def decrypt_message(msg, deck):
    decrypted_msg = ''  # Переменная для хранения расшифрованного сообщения

    for char in msg:
        while True:
            curr = deck.pop_last()  # Извлекаем последний символ из дека
            deck.push_first(curr)  # Помещаем его в начало дека
            if curr == char:  # Если символ совпадает с искомым символом
                deck.push_first(deck.pop_last())  # Извлекаем последний символ из дека и перемещаем его в начало дека
                cc = deck.pop_last()  # Извлекаем последний символ из дека
                decrypted_msg += cc  # Добавляем его к расшифрованному сообщению
                deck.push_first(cc)  # Помещаем его в начало дека
                break  # Прерываем внутренний цикл while
    return decrypted_msg  # Возвращаем расшифрованное сообщение

# Основная функция программы
def main():
    filename = "isx.txt"  # Имя файла с зашифрованным сообщением
    with open(filename, 'r') as file:
        encrypted_msg = file.read()  # Считываем зашифрованное сообщение из файла
    deck = Dequeue()  # Создаем экземпляр класса Dequeue

    # Заполняем дек символами для шифрования
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']:
        deck.push_last(c)

    decrypted_msg = decrypt_message(encrypted_msg, deck)  # Расшифровываем сообщение

    print("Расшифрованное сообщение:")
    print(decrypted_msg)  # Выводим расшифрованное сообщение на экран

    with open("res.txt", 'w') as file:
        file.write(decrypted_msg)  # Записываем расшифрованное сообщение в файл

if name == "main":
    main()  # Вызываем основную функцию программы
