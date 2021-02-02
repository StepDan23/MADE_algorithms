import operator

_DECREASE_FACTOR = 4
_DECREASE_VAL = 0.5
_INCREASE_VAL = 2


class Stack:
    def __init__(self, size=20):
        self.capacity = size
        self.arr = [0] * size
        self.last = 0

    def resize(self, n_times):
        self.capacity = int(self.capacity * n_times)
        new_arr = [0] * self.capacity
        for i in range(self.last):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def push(self, data):
        self.arr[self.last] = data
        self.last += 1
        if self.last == self.capacity:
            self.resize(n_times=_INCREASE_VAL)

    def pop(self):
        self.last -= 1
        pop_val = self.arr[self.last]

        if self.last < self.capacity / _DECREASE_FACTOR:
            self.resize(n_times=_DECREASE_VAL)

        return pop_val


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

stack = Stack(2)
inp_str = input().split()
for char in inp_str:
    if char in ops:
        b, a = stack.pop(), stack.pop()
        stack.push(ops[char](a, b))
    else:
        stack.push(int(char))
print(stack.pop())

# 8 9 + 1 7 - *
# -102
# 1 2 3 + 4 * +
# 25