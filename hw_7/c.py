import sys

_MAX_SIZE = 500_001


class FenwickTree:
    def __init__(self, arr):
        self.arr = arr
        self.t_arr = [0 for _ in range(_MAX_SIZE)]
        self.size = _MAX_SIZE
        for i in range(len(arr)):
            self.add(i, arr[i])

    def add(self, ind, val):
        j = ind
        while j < self.size:
            self.t_arr[j] += val
            j = j | (j + 1)

    def set(self, ind, val):
        d = val - self.arr[ind]
        self.arr[ind] = val
        self.add(ind, d)

    def get(self, ind):
        result = 0
        while ind >= 0:
            result += self.t_arr[ind]
            ind = (ind & (ind + 1)) - 1
        return result

    def rsq(self, left, right):
        if left == 0:
            return self.get(right)
        return self.get(right) - self.get(left - 1)


_INPUT_LINES = sys.stdin.read().splitlines()
init_arr = list(map(int, _INPUT_LINES[1].split()))
tree = FenwickTree(init_arr)
for line in _INPUT_LINES[2:]:
    cmd, ind_1, ind_2 = line.split()
    ind_1, ind_2 = int(ind_1), int(ind_2)
    if cmd == 'sum':
        print(tree.rsq(ind_1 - 1, ind_2 - 1))
    elif cmd == 'set':
        tree.set(ind_1 - 1, ind_2)
    else:
        raise ValueError('unknown operation')

# входные данныеСкопировать
# 5
# 1 2 3 4 5
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
# set 1 10
# set 2 3
# set 5 2
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
# выходные данныеСкопировать
# 14
# 15
# 10
# 9
# 12
# 22
# 20
# 10