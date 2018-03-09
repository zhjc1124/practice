class Node(object):
    def __init__(self, value=None):
        self.next = None
        self.value = value


class List(object):
    """
    List() -> new empty list
    List(iterable) -> new list initialized from iterable's items
    """
    def __add__(self, other):
        """Return self + other."""
        result = self.copy()
        result += other
        return result

    def __bool__(self):
        return not self.length

    def __contains__(self, item):
        """Return item in self."""
        p = self.head
        while p:
            if p.value == item:
                return True
        return False

    def __delitem__(self, key):
        """DO del self[key]."""
        if type(key) == int:
            if key < self.length:
                if key == 0:
                    self.head = self.head.next
                else:
                    p = self.head
                    node = 1
                    while p.next:
                        if key == node:
                            break
                        p = p.next
                        node += 1
                    p.next = p.next.next
                self.length -= 1
            else:
                raise IndexError('list assignment index out of range')
        elif type(key) == slice:
            step = key.step or 1
            index = (step > 0) - 1
            start = key.start
            if start is None:
                start = [0, self.length-1][step < 0]
            elif start <= -self.length:
                start = index
            elif start < 0:
                start += self.length
            elif start >= self.length:
                start = self.length + index
            stop = key.stop
            if stop is None:
                stop = [self.length, -1][step < 0]
            elif stop <= -self.length:
                stop = 0
            elif stop < 0:
                stop += self.length
            elif stop >= self.length:
                stop = self.length
            targets = list(range(start, stop, step))
            base = Node()
            p = base
            p.next = self.head
            node = 0
            # if step < 0 , pop the value of targets from the last
            self.length -= len(targets)
            while targets:
                if node == targets[index]:
                    p.next = p.next.next
                    targets.pop(index)
                else:
                    p = p.next
                node += 1
            self.head = base.next

        else:
            raise TypeError('list indices must be integers or slices, not %s' % key)

    def __eq__(self, other):
        """Return self==other."""
        if type(self) == type(other) and len(self) == len(other):
            sp = self.head
            op = other.head
            while True:
                if not sp and not op:
                    # sp and op are both None.
                    break
                elif sp and op:
                    if sp.value != op.value:
                        return False
                else:
                    return False
                sp = sp.next
                op = op.next
            return True
        else:
            return False

    def __ge__(self, other):
        """Return self>=other."""
        if type(other) == List:
            sp = self.head
            op = other.head
            while True:
                if sp and op:
                    if sp.value > op.value:
                        return True
                    elif sp.value < op.value:
                        return False
                elif not sp:
                    return False
                else:
                    return True
                sp = sp.next
                op = op.next
        else:
            raise TypeError("'>=' not supported between instances of 'List' and '%s'" % type(other))

    def __getattr__(self, item):
        """Return getattr(self, item)."""
        return getattr(super(), item)

    def __getitem__(self, key):
        """Return self[key]"""
        if type(key) == int:
            if not self and key < self.length:
                p = self.head
                node = 0
                while node < key:
                    p = p.next
                    node += 1
                return p.value
            else:
                raise IndexError('list index out of range')
        elif type(key) == slice:
            step = key.step or 1
            start = key.start
            if start is None:
                start = [0, self.length-1][step < 0]
            elif start <= -self.length:
                start = 0
            elif start < 0:
                start += self.length
            stop = key.stop
            if stop is None:
                stop = [self.length, -1][step < 0]
            elif stop <= -self.length:
                stop = 0
            elif stop < 0:
                stop += self.length
            targets = [i for i in range(start, stop, step) if i in range(self.length)]
            result = List()
            result.head = Node()
            rp = result.head
            p = self.head
            node = 0
            # if step < 0 , pop the value of targets from the last
            index = (step > 0)-1
            while targets:
                if node == targets[index]:
                    rp.next = Node(p.value)
                    rp = rp.next
                    targets.pop(index)
                p = p.next
                node += 1
            result.head = result.head.next
            if step < 0:
                result.reverse()
            return result
        else:
            raise TypeError('list indices must be integers or slices, not %s' % index)

    def __gt__(self, other):
        """Return self>other."""
        if type(other) == List:
            sp = self.head
            op = other.head
            while True:
                if sp and op:
                    if sp.value > op.value:
                        return True
                    elif sp.value < op.value:
                        return False
                elif not op:
                    return True
                else:
                    return False
                sp = sp.next
                op = op.next
        else:
            raise TypeError("'>=' not supported between instances of 'List' and '%s'" % type(other))

    def __iadd__(self, other):
        """Implement self+=other."""
        if type(other) == List:
            p = self.head
            while p.next:
                p = p.next
            for value in other:
                p.next = Node(value)
                p = p.next
                self.length += 1
        else:
            raise TypeError('can only concatenate list (not "%s") to list' % type(other))
        return self

    def __imul__(self, other):
        """Implement self*=other."""
        if type(other) == int:
            p = Node()
            p.next = self.head
            while p.next:
                p = p.next
            self_ = self.copy()
            for i in range(other-1):
                sp = self_.head
                while sp:
                    p.next = Node(sp.value)
                    p = p.next
                    sp = sp.next
            self.length *= other
            return self
        else:
            raise TypeError("can't multiply sequence by non-int of type '%s'" % type(other))

    def __init__(self, *values):
        self.head = None
        self.length = 0
        if len(values) == 1:
            values = values[0]
            if hasattr(values, '__iter__'):
                self.head = Node()
                p = self.head
                for value in values:
                    p.next = Node(value)
                    p = p.next
                    self.length += 1
                self.head = self.head.next
            else:
                raise TypeError("'%s' object is not iterable" % type(values))

    def __iter__(self):
        """Implement iter(self)."""
        p = self.head
        while p:
            yield p.value
            p = p.next

    def __le__(self, other):
        """Return self<=other."""
        if type(other) == List:
            return other >= self
        else:
            raise TypeError("'<=' not supported between instances of 'List' and '%s'" % type(other))

    def __len__(self):
        """Return len(self)."""
        return self.length

    def __lt__(self, other):
        """Return self<other."""
        if type(other) == List:
            return other > self
        else:
            raise TypeError("'<' not supported between instances of 'List' and '%s'" % type(other))

    def __mul__(self, other):
        """Return self*other."""
        if type(other) == int:
            self_ = self.copy()
            p = Node()
            p.next = self_.head
            while p.next:
                p = p.next
            for i in range(other-1):
                sp = self.head
                while sp:
                    p.next = Node(sp.value)
                    p = p.next
                    sp = sp.next
            self_.length *= other
            return self_
        else:
            raise TypeError("can't multiply sequence by non-int of type '%s'" % type(other))

    def __ne__(self, other):
        """Return self != other."""
        return not self == other

    def __repr__(self):
        """Return repr(self)."""
        p = self.head
        values = ''
        while p:
            values += str(p.value) + ', '
            p = p.next
        return '{' + values[:-2] + '}'

    def __reversed__(self):
        """L.__reversed__() -- return a reverse iterator over the list"""
        sp = self.head
        p = Node(sp.value)
        sp = sp.next
        while sp:
            tmp = Node(sp.value)
            tmp.next = p
            p = tmp
            sp = sp.next
        result = List()
        result.head = p
        return iter(result)

    __rmul__ = __mul__

    def __setitem__(self, key, value):
        """Set self[key] to value."""
        if type(key) == int:
            if not self and key < self.length:
                p = self.head
                node = 0
                while node < key:
                    p = p.next
                    node += 1
                p.value = value
            else:
                raise IndexError('list assignment index out of range')
        elif type(key) == slice:
            step = key.step or 1
            start = key.start
            if start is None:
                start = [0, self.length-1][step < 0]
            stop = key.stop
            if stop is None:
                stop = [self.length, -1][step < 0]
            targets = [i for i in range(start, stop, step) if i in range(self.length)]
            if hasattr(value, '__iter__'):
                index = (step > 0) - 1
                if step != 1:
                    if len(value) == len(targets):
                        p = self.head
                        node = 0
                        while targets:
                            if node == targets[index]:
                                p.value = value[index]
                                value.pop(index)
                                targets.pop(index)
                            p = p.next
                            node += 1
                    else:
                        raise ValueError('attempt to assign sequence of size %d to extended slice of size %d'
                                         % (len(value), len(targets)))
                else:
                    pass
            else:
                if step != 1:
                    raise TypeError("must assign iterable to extended slice")
                else:
                    raise TypeError("can only assign an iterable")
        else:
            raise TypeError('list indices must be integers or slices, not %s' % type(key))

    def append(self, value):
        """L.append(value) -> None -- append value to end"""
        p = self.head
        if self:
            self.head = Node(value)
        else:
            while p.next:
                p = p.next
            p.next = Node(value)
        self.length += 1
        return self

    def clear(self):
        """L.clear() -> None -- remove all items from L"""
        self.head = None

    def copy(self):
        """L.copy() -> list -- a shallow copy of L"""
        return List(self)

    def count(self, value):
        """L.count(value) -> integer -- return number of occurrences of value"""
        p = self.head
        count = 0
        while p:
            if p.value == value:
                count += 1
            p = p.next
        return count

    def extend(self, other):
        """L.extend(iterable) -> None -- extend list by appending elements from the iterable"""
        if not self:
            self.head = List(other).head
        else:
            p = self.head
            while p.next:
                p = p.next
            for i in other:
                p.next = Node(i)
                p = p.next

    def index(self):
        """L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present."""
        pass

    def insert(self):
        """L.insert(index, object) -- insert object before index"""
        pass

    def pop(self):
        """L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range."""
        pass

    def remove(self):
        """L.remove(value) -> None -- remove first occurrence of value.
        Raises ValueError if the value is not present."""
        pass

    def reverse(self):
        """L.reverse() -- reverse *IN PLACE*"""
        pre = self.head
        p = pre.next
        suf = p.next

        self.head.next = None
        self.head = None
        while suf:
            p.next = pre
            pre = p
            p = suf
            suf = p.next
        p.next = pre
        self.head = p

    def sort(self):
        """L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*"""
        pass


# a,b,c=-17,-25,-4
a,b,c=-24,None,-17
L = List(range(10))
ll = list(range(10))
del L[a:b:c]
del ll[a:b:c]
print(L==List(ll))
l = list(range(-30, 30))
l.append(None)
import random
for i in range(10000):
    a = random.choice(l)
    b = random.choice(l)
    c = random.choice(l)
    if c == 0:
        c = None
    T1 = List(range(10))
    T2 = list(range(10))
    del T1[a:b:c]
    del T2[a:b:c]
    if T1 != List(T2):
        print(a, b, c, T1, T2)
