import sys

_MAX_SAMPLES = 10 ** 5


class ListNode:
    def __init__(self, key=None, val='none', prev_map=None, next_map=None):
        self.key = key
        self.val = val
        self.next_node = None
        self.prev_map = prev_map
        self.next_map = next_map

    def set(self, key, val, prev_map, next_map, next_node):
        self.key = key
        self.val = val
        self.prev_map = prev_map
        self.next_map = next_map
        self.next_node = next_node


class CustomLinkedMap:

    def __init__(self, arr_size, alpha=93, betta=2147483647):
        self.alpha = alpha
        self.betta = betta
        self.arr_size = arr_size
        self.hash_arr = [ListNode() for _ in range(arr_size)]
        self.curr_node = ListNode(prev_map=ListNode())

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
                iter_node.set(key_val, str_val, prev_map=self.curr_node, next_map=ListNode(), next_node=ListNode())
                self.curr_node.next_map = iter_node
                self.curr_node = iter_node
                return 'new'
            elif iter_node.key == key_val:
                iter_node.val = str_val
                return 'overwrite'
            else:
                iter_node = iter_node.next_node

    def delete(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        if self.curr_node.key == key_val:
            self.curr_node = self.curr_node.prev_map  # delete in map_list
        if iter_node.key == key_val:
            iter_node.next_map.prev_map = iter_node.prev_map  # delete in map_list
            iter_node.prev_map.next_map = iter_node.next_map  # delete in map_list
            self.hash_arr[hash_key_val] = iter_node.next_node  # delete in node_list
            return 'first'
        while iter_node.next_node:
            if iter_node.next_node.key == key_val:
                iter_node.next_node.prev_map.next_map = iter_node.next_node.next_map  # delete in map_list
                iter_node.next_node.next_map.prev_map = iter_node.next_node.prev_map  # delete in map_list
                iter_node.next_node = iter_node.next_node.next_node  # delete in node_list
                return 'in_list'
            else:
                iter_node = iter_node.next_node
        return 'missing'

    def get(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while True:
            if iter_node.key is None:
                return 'none'
            elif iter_node.key == key_val:
                return iter_node.val
            else:
                iter_node = iter_node.next_node

    def prev(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while iter_node.key != key_val:
            if iter_node.key is None:
                return 'none'
            iter_node = iter_node.next_node

        return iter_node.prev_map.val

    def next(self, key_val):
        hash_key_val = self.hash_function(key_val)
        iter_node = self.hash_arr[hash_key_val]

        while iter_node.key != key_val:
            if iter_node.key is None:
                return 'none'
            iter_node = iter_node.next_node

        return iter_node.next_map.val


size = _MAX_SAMPLES * 2
my_map = CustomLinkedMap(size, alpha=7, betta=193877777)
_INPUT_LINES = sys.stdin.buffer.read().decode().splitlines()
output = []
for line in _INPUT_LINES:
    opp_arr = line.split()
    if opp_arr[0] == 'put':
        my_map.insert(opp_arr[1], opp_arr[2])
    elif opp_arr[0] == 'delete':
        my_map.delete(opp_arr[1])
    elif opp_arr[0] == 'get':
        output.append(my_map.get(opp_arr[1]))
    elif opp_arr[0] == 'prev':
        output.append(my_map.prev(opp_arr[1]))
    elif opp_arr[0] == 'next':
        output.append(my_map.next(opp_arr[1]))
    else:
        raise ValueError('unknown operation')
sys.stdout.buffer.write('\n'.join(output).encode())


my_map.prev('one')
my_map.next('one')

my_map.insert('one', 1)
my_map.insert('three', 3)
my_map.delete('three')
my_map.next('three')
my_map.insert('two', 2)
my_map.prev('two')

my_map.insert('two', 2)

my_map.prev('two')
my_map.next('two')

my_map.next('three')
my_map.prev('three')

my_map.delete('one')
my_map.get('three')
my_map.delete('two')
my_map.get('two')

# входные данныеСкопировать
# put zero a
# put one b
# put two c
# put three d
# put four e
# get two
# prev two
# next two
# delete one
# delete three
# get two
# prev two
# next two
# next four
# выходные данныеСкопировать
# c
# b
# d
# c
# a
# e
# none


# put two e
# put two b
# put three m
# put four f
# delete three
# next two
# prev two
# put two h
# next four
# delete three
# get two
# prev two
# next two

# f
# none
# none
# h
# none
# f