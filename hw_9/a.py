import sys
from random import randint

MAX_N = 10_000

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def merge(self, t_1, t_2):
        if t_1 is None:
            return t_2
        elif t_2 is None:
            return t_1
        if t_1.y > t_2.y:
            t_1.right = self.merge(t_1.right, t_2)
            return t_1
        else:
            t_2.left = self.merge(t_1, t_2.left)
            return t_2

    def split(self, vert, x_split):
        if vert is None:
            return None, None
        if vert.x > x_split:
            t_1, t_2 = self.split(vert.left, x_split)
            vert.left = t_2
            return t_1, vert
        else:
            t_1, t_2 = self.split(vert.right, x_split)
            vert.right = t_1
            return vert, t_2

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, randint(0, MAX_N))
        else:
            t_1, t_2 = self.split(self.root, value)
            t_1 = self.merge(t_1, Node(value, randint(0, MAX_N)))
            self.root = self.merge(t_1, t_2)

    def remove(self, value):
        t_1, t_2 = self.split(self.root, value)
        t_11, t_12 = self.split(t_1, value - 1)
        self.root = self.merge(t_11, t_2)

    def _find(self, vert, value):
        if vert is None or vert.x == value:
            return vert
        elif vert.x < value:
            return self._find(vert.right, value)
        else:
            return self._find(vert.left, value)

    def find(self, value):
        return not(self._find(self.root, value) is None)

    def prev(self, value):
        t_1, t_2 = self.split(self.root, value - 1)
        if t_1 is None:
            return None
        iter_node = t_1
        while iter_node.right:
            iter_node = iter_node.right
        prev_val = iter_node.x
        self.root = self.merge(t_1, t_2)
        return prev_val

    def next(self, value):
        t_1, t_2 = self.split(self.root, value)
        if t_2 is None:
            return None
        iter_node = t_2
        while iter_node.left:
            iter_node = iter_node.left
        next_val = iter_node.x
        self.root = self.merge(t_1, t_2)
        return next_val


tree = Treap()
for line in sys.stdin.read().splitlines():
    command, value = line.split()
    value = int(value)
    if command == 'insert':
        tree.insert(value)
    elif command == 'delete':
        tree.remove(value)
    elif command == 'exists':
        print(str(tree.find(value)).lower())
    elif command == 'next':
        print(str(tree.next(value)).lower())
    elif command == 'prev':
        print(str(tree.prev(value)).lower())
    else:
        raise ValueError('Unknown command')

#
# true
# false
# 5
# 3
# none
# 3