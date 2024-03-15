В данной работе  были реализованны следующие структуры данных:

● Стек (stack):

Операции для стека: инициализация, проверка на пустоту, добавление нового элемента в начало, извлечение элемента из начала;

● Дек (двусторонняя очередь, deque):

Операции для дека: инициализация, проверка на пустоту, добавление нового элемента в начало, добавление нового элемента в конец, извлечение элемента из начала, извлечение элемента из конца.

Были разработаны программы обработки данных, с заранее подготовленными txt-файлами, в соответствии со следующими заданиями:
Задание №1 (каталог zad1)
Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.

Задание №2 (каталог zad2)
Дек содержит последовательность символов для шифровки сообщений. Дан текстовый файл, содержащий зашифрованное сообщение. Пользуясь деком, расшифровать текст. Известно, что при
шифровке каждый символ сообщения заменялся следующим за ним в деке по часовой стрелке через один.

Задание №3 (каталог zad3)
Даны три стержня и n дисков различного размера. Диски можно надевать на стержни, образуя из них башни. Перенести n дисков со стержня А на стержень С, сохранив их первоначальный
порядок. При переносе дисков необходимо соблюдать следующие правила:
- на каждом шаге со стержня на стержень переносить только один диск;
- диск нельзя помещать на диск меньшего размера;
- для промежуточного хранения можно использовать стержень В.
- Реализовать алгоритм, используя три стека вместо стержней А, В, С. Информация о дисках хранится в исходном файле.

Задание №4 (каталог zad4)
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс круглых скобок в тексте, используя стек.

Задание №5 (каталог zad5)
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс квадратных скобок в тексте, используя дек.

Задание №6 (каталог zad6)
Дан файл из символов. Используя стек, за один просмотр файла напечатать сначала все цифры, затем все буквы, и, наконец, все остальные символы, сохраняя исходный порядок в каждой группе символов.

Задание №7 (каталог zad7)
Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа, затем все положительные числа, сохраняя исходный порядок в каждой группе.

Задание №8 (каталог zad8)
Дан текстовый файл. Используя стек, сформировать новый текстовый файл, содержащий строки исходного файла, записанные в обратном порядке: первая строка становится последней, вторая – предпоследней и т.д.

В каждом каталоге имеется рабочий код в файле .py, изначальный txt документ с изначальными входными данными, а также txt документ с результатами выполнения кода.
