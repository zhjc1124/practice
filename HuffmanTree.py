class HTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


values = [2, 3, 7, 10, 4, 2, 5]
HTNodes = [HTNode(value) for value in values]
for t in HTNodes:
    print(t.value, end=' ')
print()
while len(HTNodes) > 1:
    HTNodes.sort()
    for t in HTNodes:
        print(t.value, end=' ')
    print()
    left = HTNodes.pop(0)
    right = HTNodes[0]
    v = left.value + right.value
    HTNodes[0] = HTNode(value=v, left=left, right=right)
    for t in HTNodes:
        print(t.value, end=' ')
    print()

