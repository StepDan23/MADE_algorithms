import sys


class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def check_size(self):
        if self.size > 0:
            return True
        return False

    def sift_up(self, ind):
        while ind > 0 and self.arr[ind][0] <= self.arr[(ind - 1) // 2][0]:
            self.arr[ind], self.arr[(ind - 1) // 2] = self.arr[(ind - 1) // 2], self.arr[ind]
            ind = (ind - 1) // 2
        return ind

    def sift_down(self, ind):
        while 2 * ind + 1 < self.size:
            curr = self.arr[ind][0]
            left = self.arr[2 * ind + 1][0]
            if 2 * ind + 2 == self.size:
                right = float('inf')
            else:
                right = self.arr[2 * ind + 2][0]
            if left <= right and left <= curr:
                self.arr[ind], self.arr[2 * ind + 1] = self.arr[2 * ind + 1], self.arr[ind]  # swap left, curr
                ind = 2 * ind + 1
            elif right <= left and right <= curr:
                self.arr[ind], self.arr[2 * ind + 2] = self.arr[2 * ind + 2], self.arr[ind]  # swap right, curr
                ind = 2 * ind + 2
            else:
                return ind

    def push(self, data):
        self.arr.append(data)
        self.size += 1
        self.sift_up(self.size - 1)

    def pop(self):
        if self.size:
            self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
            self.size -= 1
            self.sift_down(0)
            return self.arr.pop()
        else:
            return ['*']

    def replace_key(self, index, val):
        j = 0
        while j < self.size and self.arr[j][1] != index:
            j += 1
        if j != self.size:
            self.arr[j][0] = val
            self.sift_up(j)


heap = Heap()
_INPUT_LINES = sys.stdin.read().splitlines()
for i, line in enumerate(_INPUT_LINES):
    if line[:4] == 'push':
        heap.push([int(line[5:]), i + 1])
    elif line[:11] == 'extract-min':
        print(*heap.pop())
    elif line[:12] == 'decrease-key':
        key, value = map(int, line[13:].split())
        heap.replace_key(key, value)
    else:
        raise ValueError('unknown operation')

# extract-min
# push 3
# push 4
# push 2
# extract-min
# decrease-key 2 1
# extract-min
# extract-min
# extract-min
#
# 2 3
# 1 2
# 3 1
# *