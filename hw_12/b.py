import sys


class Vert:
    def __init__(self, value):
        self.exp = 0
        self.parent = value
        self.count = 1


class SNM:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.vert_list = [Vert(i) for i in range(n_vert + 1)]

    def add(self, vert_id, value):
        """add exp to vert_id or to parent of vert_id only"""
        vert = self.vert_list[vert_id]
        parent_vert, parent_exp = self.get(vert.parent)
        parent_vert.exp += value

    def get(self, vert_id):
        """return parent vertex and exp for vert_id"""
        vert = self.vert_list[vert_id]
        cur_exp = vert.exp
        if vert_id != vert.parent:
            parent_vert, parent_exp = self.get(vert.parent)
            cur_exp += parent_exp
            vert.parent = parent_vert.parent  # id of parent vert
            # save the same cur_exp with another parent
            vert.exp = cur_exp - self.vert_list[parent_vert.parent].exp
        return self.vert_list[vert.parent], cur_exp

    def join(self, vert_id_1, vert_id_2):
        vert_1, _ = self.get(vert_id_1)
        vert_2, _ = self.get(vert_id_2)
        if vert_1.parent != vert_2.parent:
            if vert_2.count > vert_1.count:
                vert_1, vert_2 = vert_2, vert_1
            vert_2.parent = vert_1.parent
            vert_2.exp -= vert_1.exp
            vert_1.count += vert_2.count


_INPUT_LINES = sys.stdin.read().splitlines()
n_vert, _ = map(int, _INPUT_LINES[0].split())
my_snm = SNM(n_vert)
for line in _INPUT_LINES[1:]:
    command, values = line.split(maxsplit=1)
    if command == 'add':
        vert_id, exp = map(int, values.split())
        my_snm.add(vert_id, exp)
    elif command == 'join':
        id_1, id_2 = map(int, values.split())
        my_snm.join(id_1, id_2)
    elif command == 'get':
        _, exp = my_snm.get(int(values))
        print(exp)
    else:
        raise ValueError('unknown command')
