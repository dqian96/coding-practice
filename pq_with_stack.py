from collections import namedtuple


Node = namedtuple('Node', 'value priority')


class PriorityQueue:
    def __init__(self):

        self.stack = []

    def add(self, value, priority):
        temp_stack = []

        while len(self.stack) != 0 and self.stack[-1].priority < priority:
            temp_stack.append(self.stack.pop())

        self.stack.append(Node(value, priority))

        while len(temp_stack) != 0:
            self.stack.append(temp_stack.pop())

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop().value

    def is_empty(self):
        return len(self.stack) == 0


def test():
    pq = PriorityQueue()

    pq.add(3, 3)
    pq.add(2, 2)
    pq.add(1, 1)

    while not pq.is_empty():
        print(pq.pop())


if __name__ == '__main__':
    test()
