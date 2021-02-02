import sys

_MAX_SAMPLES = 10 ** 5
_EMPTY_VAL = -1
_DELETE_VAL = -2


class ListNode:
    def __init__(self, key=None, set_val=None, next_node=None):
        self.key = key
        self.set_val = set_val
        self.next_node = next_node

    def set(self, key=None, set_val=None, next_node=None):
        self.key = key
        self.set_val = set_val
        self.next_node = next_node


class CustomSet:
    def __init__(self, arr_size, alpha=93, betta=2147483647):
        self.alpha = alpha
        self.betta = betta
        self.size = 0
        self.capacity = arr_size
        self.hash_arr = [_EMPTY_VAL for _ in range(arr_size)]

    def hash_function(self, str_val):
        hash_val = 0
        for char_val in str_val:
            hash_val = (hash_val * self.alpha + ord(char_val)) % self.betta
        return hash_val % self.capacity

    def resize(self, coef=2):
        self.capacity *= coef
        old_arr = self.hash_arr
        self.hash_arr = [_EMPTY_VAL for _ in range(self.capacity)]
        self.size = 0
        for val in old_arr:
            if val != _EMPTY_VAL and val != _DELETE_VAL:
                self.insert(val)

    def insert(self, val):
        hash_val = self.hash_function(val)
        is_insert = False
        while not is_insert:
            cur_val = self.hash_arr[hash_val]
            if cur_val == _EMPTY_VAL or cur_val == _DELETE_VAL:
                self.hash_arr[hash_val] = val
                self.size += 1
                is_insert = True
            elif cur_val == val:
                is_insert = True
            else:
                hash_val = (hash_val + 1) % self.capacity
        if self.size > self.capacity // 2:
            self.resize()

    def delete(self, val):
        hash_val = self.hash_function(val)
        is_delete = False
        while not is_delete:
            cur_val = self.hash_arr[hash_val]
            if cur_val == _EMPTY_VAL:
                is_delete = True
            elif cur_val == val:
                self.size -= 1
                self.hash_arr[hash_val] = _DELETE_VAL
                is_delete = True
            else:
                hash_val = (hash_val + 1) % self.capacity

    def set_print(self):
        non_null_values = [val for val in self.hash_arr if val != _DELETE_VAL if val != _EMPTY_VAL]
        return str(self.size) + ' ' + ' '.join(non_null_values)


class CustomMultiMap:

    def __init__(self, arr_size, alpha=93, betta=2147483647):
        self.alpha = alpha
        self.betta = betta
        self.arr_size = arr_size
        self.hash_arr = [ListNode(next_node=ListNode()) for _ in range(arr_size)]

    def hash_function(self, str_val):
        hash_val = 0
        for char_val in str_val:
            hash_val = (hash_val * self.alpha + ord(char_val)) % self.betta
        return hash_val % self.arr_size

    def insert(self, key_val, str_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while True:
            if iter_node.key is None:
                iter_node.set(key_val, set_val=CustomSet(100), next_node=ListNode())
                iter_node.set_val.insert(str_val)
                return 'new'
            elif iter_node.key == key_val:
                iter_node.set_val.insert(str_val)
                return 'append'
            else:
                iter_node = iter_node.next_node

    def get(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while iter_node.key is not None:
            if iter_node.key == key_val:
                return iter_node.set_val.set_print()
            iter_node = iter_node.next_node
        return '0'

    def delete(self, key_val, str_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while iter_node.key is not None:
            if iter_node.key == key_val:
                iter_node.set_val.delete(str_val)
                return 'in_list'
            else:
                iter_node = iter_node.next_node
        return 'missing'

    def delete_all(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while iter_node.key is not None:
            if iter_node.key == key_val:
                iter_node.set_val = CustomSet(100)
                return True
            iter_node = iter_node.next_node


size = _MAX_SAMPLES * 2
my_map = CustomMultiMap(size, alpha=7, betta=193877777)
_INPUT_LINES = sys.stdin.buffer.read().decode().splitlines()
output = []
for line in _INPUT_LINES:
    opp_arr = line.split()
    if opp_arr[0] == 'put':
        my_map.insert(opp_arr[1], opp_arr[2])
    elif opp_arr[0] == 'get':
        output.append(my_map.get(opp_arr[1]))
    elif opp_arr[0] == 'delete':
        my_map.delete(opp_arr[1], opp_arr[2])
    elif opp_arr[0] == 'deleteall':
        my_map.delete_all(opp_arr[1])
    else:
        raise ValueError('unknown operation')
sys.stdout.buffer.write('\n'.join(output).encode())


# входные данныеСкопировать
# put a a
# put a b
# put a c
# get a
# delete a b
# get a
# deleteall a
# get a
# выходные данныеСкопировать
# 3 a b c
# 2 a c
# 0

for i in range(100):
    my_map.insert('a', str(i))