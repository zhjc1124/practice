class Heap(object):
    def __init__(self, values):
        self._values = []
        for value in values:
            self.sift_up(value)

    def __len__(self):
        return len(self._values)

    def sift_up(self, value):
        values = self._values
        values.append(value)
        index = len(self) - 1
        while index:
            i, j = (index - 1) // 2, index
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
                index = i
            else:
                break

    def pop(self):
        start = self._values[0]
        end = self._values.pop()
        if len(self):
            self._values[0] = end
            self.sift_down()
        return start

    def is_empty(self):
        return not bool(self._values)

    def sift_down(self):
        index = 0
        values = self._values
        while 2 * index + 1 < len(self) - 1:
            i, j = index, 2 * index + 1
            if j + 1 < len(self) and values[j + 1] < values[j]:
                j += 1
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
                index = j
            else:
                break


if __name__ == "__main__":
    h = Heap([1, 5, 5, 2, 3, 8, 34, 12, 23, 4, 6, 7, 3])
    while not h.is_empty():
        print(h.pop(), end=' ')
