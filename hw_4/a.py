import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.start = None
        self.min_val = float('inf')
        self.min_count = 0

    def _find_min(self):
        iter_node = self.start
        self.min_val = float('inf')

        while iter_node:
            if self.min_val > iter_node.data:
                self.min_val = iter_node.data
                self.min_count = 1
            elif self.min_val == iter_node.data:
                self.min_count += 1
            iter_node = iter_node.next

    def push(self, data):
        data_node = Node(data)
        data_node.next = self.start
        self.start = data_node

        if data < self.min_val:
            self.min_val = data
            self.min_count = 1
        elif data == self.min_val:
            self.min_count += 1

    def pop(self):
        pop_node = self.start
        self.start = pop_node.next

        if self.min_val == pop_node.data:
            if self.min_count == 1:
                self._find_min()
            else:
                self.min_count -= 1
        return pop_node.data


stack = Stack()
_INPUT_LINES = sys.stdin.read().splitlines()
for inp_str in _INPUT_LINES[1:]:
    if inp_str[0] == '1':
        stack.push(int(inp_str[2:]))
    elif inp_str[0] == '2':
        stack.pop()
    elif inp_str[0] == '3':
        print(stack.min_val)
    else:
        raise ValueError('unknown operation')

# 8
# 1 2
# 1 3
# 1 -3
# 3
# 2
# 3
# 2
# 3
# выходные данныеСкопировать
# -3
# 2
# 2