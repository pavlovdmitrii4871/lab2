class Node:
    def __init__(self, el):
        self.next = None
        self.prev = None
        self.el = el


class Stack:
    count: int

    last: Node | None

    def __init__(self):
        self.last = None
        self.count = 0

    def push(self, el):
        node = Node(el)
        self.count += 1
        if self.last:
            self.last.next = node
            node.prev = self.last
        self.last = node

    def pop(self):
        if self.last:
            el = self.last.el
            self.last = self.last.prev
            self.count -= 1
            return el
        else:
            raise IndexError

    def get_last(self):
        return self.last.el

    def __len__(self):
        return self.count

class Dequeue:
    count: int

    first: Node | None
    last: Node | None

    def __init__(self):
        self.count = 0

        self.first = None
        self.last = None

    def push_first(self, el):
        node = Node(el)
        if self.first:
            node.next = self.first
            self.first.prev = node
        if not self.last:
            self.last = node
        self.first = node
        self.count += 1

    def push_last(self, el):
        node = Node(el)
        if self.last:
            self.last.next = node
            node.prev = self.last
        if not self.first:
            self.first = node
        self.last = node
        self.count += 1

    def pop_last(self):
        if self.last:
            el = self.last.el
            self.last = self.last.prev
            self.count -= 1
            return el
        else:
            raise IndexError

    def pop_first(self):
        if self.first:
            el = self.first.el
            self.first = self.first.next
            self.count -= 1
            return el
        else:
            raise IndexError

    def __len__(self):
        return self.count
