import sys

_MAX_SAMPLES = 10 ** 6
_EMPTY_VAL = int(1e9) + 1
_DELETE_VAL = int(1e9) + 2


class CustomSet:

    def __init__(self, arr_size, alpha=93, betta=2147483647):
        self.alpha = alpha
        self.betta = betta
        self.arr_size = arr_size
        self.hash_arr = [_EMPTY_VAL for _ in range(arr_size)]

    def hash_function(self, val):
        return ((self.alpha * val) % self.betta) % self.arr_size

    def insert(self, val):
        hash_val = self.hash_function(val)
        is_insert = False
        while not is_insert:
            cur_val = self.hash_arr[hash_val]
            if cur_val == _EMPTY_VAL or cur_val == _DELETE_VAL or cur_val == val:
                self.hash_arr[hash_val] = val
                is_insert = True
            else:
                hash_val = (hash_val + 1) % self.arr_size

    def delete(self, val):
        hash_val = self.hash_function(val)
        is_delete = False
        while not is_delete:
            cur_val = self.hash_arr[hash_val]
            if cur_val == _EMPTY_VAL:
                is_delete = True
            elif cur_val == val:
                self.hash_arr[hash_val] = _DELETE_VAL
                is_delete = True
            else:
                hash_val = (hash_val + 1) % self.arr_size

    def exist(self, val):
        hash_val = self.hash_function(val)
        while True:
            cur_val = self.hash_arr[hash_val]
            if cur_val == _EMPTY_VAL:
                return 'false'
            elif cur_val == val:
                return 'true'
            else:
                hash_val = (hash_val + 1) % self.arr_size


size = _MAX_SAMPLES * 2
my_set = CustomSet(size, alpha=7, betta=193877777)
_INPUT_LINES = sys.stdin.buffer.read().decode().splitlines()
output = []
for line in _INPUT_LINES:
    opp, num = line.split()
    num = int(num)
    if opp == 'insert':
        my_set.insert(num)
    elif opp == 'delete':
        my_set.delete(num)
    elif opp == 'exists':
        output.append(my_set.exist(num))
    else:
        raise ValueError('unknown operation')
sys.stdout.buffer.write('\n'.join(output).encode())
