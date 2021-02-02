import sys
from random import randint

MAX_N = 100_000_000


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 1
        self.left = None
        self.right = None

    def get_left_size(self):
        if self.left is None:
            return 0
        return self.left.size

    def get_right_size(self):
        if self.right is None:
            return 0
        return self.right.size

    def fix(self):
        self.size = self.get_left_size() + self.get_right_size() + 1
        return self


class ImplicitTreap:
    def __init__(self):
        self.root = None

    def merge(self, t_1, t_2):
        if t_1 is None:
            return t_2
        elif t_2 is None:
            return t_1
        if t_1.y > t_2.y:
            t_1.right = self.merge(t_1.right, t_2)
            return t_1.fix()
        else:
            t_2.left = self.merge(t_1, t_2.left)
            return t_2.fix()

    def split(self, vert, x_split):
        if vert is None:
            return None, None
        if vert.get_left_size() > x_split:
            t_1, t_2 = self.split(vert.left, x_split)
            vert.left = t_2
            vert = vert.fix()
            return t_1, vert
        else:
            t_1, t_2 = self.split(vert.right, x_split - vert.get_left_size() - 1)
            vert.right = t_1
            vert = vert.fix()
            return vert, t_2

    def insert(self, pos, value):
        if self.root is None:
            self.root = Node(value, randint(0, MAX_N))
            return
        t_1, t_2 = self.split(self.root, pos)
        t_1 = self.merge(t_1, Node(value, randint(0, MAX_N)))
        self.root = self.merge(t_1, t_2)

    def remove(self, pos):
        t_1, t_2 = self.split(self.root, pos)
        t_11, t_12 = self.split(t_1, pos - 1)
        self.root = self.merge(t_11, t_2)

    def print(self, vert):
        if vert:
            self.print(vert.left)
            print(vert.x, end=' ')
            self.print(vert.right)


INPUT_LINES = sys.stdin.read().splitlines()
tree = ImplicitTreap()
for i, val in enumerate(map(int, INPUT_LINES[1].split())):
    tree.insert(i - 1, val)
for line in INPUT_LINES[2:]:
    command, values = line.split(' ', 1)
    if command == 'add':
        pos, value = map(int, values.split())
        tree.insert(pos - 1, value)
    elif command == 'del':
        tree.remove(int(values) - 1)
    else:
        raise ValueError('Unknown command')

if tree.root is None:
    print(0)
else:
    print(tree.root.size)
    tree.print(tree.root)
