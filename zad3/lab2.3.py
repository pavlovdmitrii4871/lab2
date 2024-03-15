class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items


def hanoi(n, source, target, auxiliary):
    if n == 1:
        disk = source.pop()
        target.push(disk)
        return

    hanoi(n-1, source, auxiliary, target)

    disk = source.pop()
    target.push(disk)

    hanoi(n-1, auxiliary, target, source)


tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

input_filename = 'disks.txt'
output_filename = 'results.txt'
with open(input_filename, "r") as file:
    disks = file.read().split()

for disk in disks:
    tower_a.push(disk)

hanoi(tower_a.size(), tower_a, tower_c, tower_b)

with open(output_filename, "w") as file:
    file.write("Стержень A: " + str(tower_a.items) + "\n")
    file.write("Стержень B: " + str(tower_b.items) + "\n")
    file.write("Стержень C: " + str(tower_c.items) + "\n")

print(f"Результаты записаны в файл {output_filename}.")
