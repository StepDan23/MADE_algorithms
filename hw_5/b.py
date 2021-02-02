import sys

_MAX_SAMPLES = 10 ** 5


class CustomMap:

    def __init__(self, arr_size, alpha=93, betta=2147483647):
        self.alpha = alpha
        self.betta = betta
        self.arr_size = arr_size
        self.hash_arr = [[] for _ in range(arr_size)]

    def hash_function(self, str_val):
        hash_val = 0
        for char_val in str_val:
            hash_val = (hash_val * self.alpha + ord(char_val)) % self.betta
        return hash_val % self.arr_size

    def insert(self, key_val, str_val):
        hash_key_val = self.hash_function(key_val)
        cur_list = self.hash_arr[hash_key_val]

        for i in range(len(cur_list)):
            key, val = cur_list[i]
            if key == key_val:
                cur_list[i][1] = str_val
                return 'overwrite'
        cur_list.append([key_val, str_val])
        return 'new'

    def delete(self, key_val):
        hash_key_val = self.hash_function(key_val)
        cur_list = self.hash_arr[hash_key_val]

        for i in range(len(cur_list)):
            key, val = cur_list[i]
            if key == key_val:
                cur_list.pop(i)
                break

    def get(self, key_val):
        hash_key_val = self.hash_function(key_val)
        cur_list = self.hash_arr[hash_key_val]

        for i in range(len(cur_list)):
            key, val = cur_list[i]
            if key == key_val:
                return val
        return 'none'

size = _MAX_SAMPLES * 2
my_map = CustomMap(size, alpha=7, betta=193877777)
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
    else:
        raise ValueError('unknown operation')
sys.stdout.buffer.write('\n'.join(output).encode())

#
# входные данныеСкопировать
# put hello privet
# put bye poka
# get hello
# get bye
# delete hello
# get hello
# выходные данныеСкопировать
# privet
# poka
# none