class Node(object):
    def __init__(self, value=0):
        self.next = None
        self.value = value


class List(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        p = self.head
        values = []
        while p:
            values.append(p.value)
            p = p.next
        return str(values)

    __repr__ = __str__

    def is_empty(self):
        return bool(not self.head)

    def append(self, value):
        p = self.head
        if self.is_empty():
            self.head = Node(value)
        else:
            while p.next:
                p = p.next
            p.next = Node(value)
        return self

    def add(self, values):
        for i in values:
            self.append(i)
        return self
    
    def get(self, index):
        if not self.is_empty():
            p = self.head
            node = 0
            while p.next and (node < index):
                p = p.next
                node += 1
            if node == index:
                return p.value
        raise IndexError('Index out of bound')
    
    def destroy(self):
        self.head = None

L = List()
