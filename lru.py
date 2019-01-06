# Simple cache using the LRU eviction policy.
# Implemented using a doubly linked list and hash table to ensure
# constant time inserts/eviction.

class _Node:
    def __init__(self, val, prev=None, nxt=None):
        self.prev, self.nxt = prev, nxt
        self.val = val


class _DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def append(self, n):
        n.prev, n.nxt = None, None

        if not self.start:
            self.start = n
            self.end = n
        else:
            self.end.nxt = n
            n.prev = self.end
            self.end = n

        self.length += 1

    def remove(self, n):
        if self.start is None:
            return

        if self.start == self.end:
            self.start, self.end = None, None
        else:
            prev = n.prev
            nxt = n.nxt

            if prev:
                prev.nxt = nxt
            else:
                self.start = nxt

            if nxt:
                nxt.prev = prev
            else:
                self.end = prev

            self.length -= 1

    def __str__(self):
        vals = []
        curr = self.start
        while curr is not None:
            vals.append(str(curr.val))
            curr = curr.nxt

        return ' -> '.join(vals)


class LRU:
    def __init__(self, limit):
        self.ht = {}
        self.ll = _DoublyLinkedList()
        self.limit = limit

    def evict(self):
        if self.ll.length == 0:
            return

        lru = self.ll.start
        self.ll.remove(lru)
        del self.ht[lru.val]

    def add(self, val):
        if self.ll.length == self.limit:
            self.evict()

        n = _Node(val)
        self.ll.append(n)
        self.ht[val] = n

    def use(self, val):
        if val not in self.ht.keys():
            self.add(val)
        else:
            n = self.ht[val]
            self.ll.remove(n)
            self.ll.append(n)

    def __str__(self):
        serialized_format = """\
            limit: {}
            order: {}
            """
        return serialized_format.format(self.limit, self.ll.__str__())


def main():
    lru = LRU(5)
    while True:
        to_add = int(input('>>> '))
        lru.use(to_add)
        print(lru)


if __name__ == '__main__':
    main()
