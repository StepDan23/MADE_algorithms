import sys

MAX_N = 100_000


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 1
        self.need_reverse = False
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


class ImplicitReverseTreap:
    def __init__(self):
        self.root = None

    def merge(self, t_1, t_2):
        self._make_reverse(t_1)
        self._make_reverse(t_2)
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
        self._make_reverse(vert)
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

    def insert(self, pos, value, prior):
        if self.root is None:
            self.root = Node(value, prior)
            return
        t_1, t_2 = self.split(self.root, pos)
        t_1 = self.merge(t_1, Node(value, prior))
        self.root = self.merge(t_1, t_2)

    @staticmethod
    def _make_reverse(vert):
        if vert and vert.need_reverse:
            vert.need_reverse = False
            vert.left, vert.right = vert.right, vert.left
            if vert.left:
                vert.left.need_reverse ^= True
            if vert.right:
                vert.right.need_reverse ^= True

    def reverse(self, start, end):
        if start != end:
            t_1, t_2 = self.split(self.root, start - 1)
            t_21, t_22 = self.split(t_2, end - start)
            t_21.need_reverse ^= True
            self._make_reverse(t_21)
            self.root = self.merge(t_1, self.merge(t_21, t_22))

    def print(self, vert):
        if vert:
            self._make_reverse(vert)
            self.print(vert.left)
            print(vert.x, end=' ')
            self.print(vert.right)


def bin_fill(arr, left, right):
    for i in range(left, right):
        arr[i] -= 1
    if left < right:
        mid = (left + right) // 2
        bin_fill(arr, left, mid)
        bin_fill(arr, mid + 1, right)


INPUT_LINES = sys.stdin.read().splitlines()
tree = ImplicitReverseTreap()
len_, _ = map(int, INPUT_LINES[0].split())
priors = [len_ for _ in range(len_)]
bin_fill(priors, 0, len_)

for i in range(len_):
    tree.insert(i, i + 1, priors[i])

for line in INPUT_LINES[1:]:
    start_, end_ = map(int, line.split())
    tree.reverse(start_ - 1, end_ - 1)
tree.print(tree.root)

# 5 3
# 2 4
# 3 5
# 2 2
# выходные данныеСкопировать
# 1 4 5 2 3
