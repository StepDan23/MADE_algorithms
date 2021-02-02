import sys

_DECREASE_FACTOR = 4
_DECREASE_VAL = 0.5
_INCREASE_VAL = 2


class Queue:
    def __init__(self, size=20):
        self.capacity = size
        self.arr = [0] * size
        self.last = 0
        self.first = 0
        self.size = 0

    def resize(self, n_times):
        old_capacity = self.capacity
        self.capacity = int(self.capacity * n_times)
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[(self.first + i) % old_capacity]
        self.arr = new_arr
        self.first = 0
        self.last = self.size

    def push(self, data):
        self.arr[self.last] = data
        self.last = (self.last + 1) % self.capacity
        self.size += 1

        if self.last == self.first:
            self.resize(n_times=_INCREASE_VAL)

    def pop(self):
        pop_val = self.arr[self.first]
        self.first = (self.first + 1) % self.capacity
        self.size -= 1

        if self.size < self.capacity / _DECREASE_FACTOR:
            self.resize(n_times=_DECREASE_VAL)

        return pop_val


queue = Queue(2)
_INPUT_LINES = sys.stdin.read().splitlines()
for line in _INPUT_LINES[1:]:
    if line[0] == '+':
        queue.push(int(line[2:]))
    elif line[0] == '-':
        print(queue.pop())
    else:
        raise ValueError('unknown operation')

#
# 4
# + 1
# + 10
# -
# -
