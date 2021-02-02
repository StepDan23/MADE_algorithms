import sys


class Vert:
    def __init__(self, value):
        self.val = value
        self.parent = value
        self.min = value
        self.max = value
        self.count = 1


class SNM:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.vert_list = [Vert(i) for i in range(n_vert + 1)]

    def get(self, vert_id):
        vert = self.vert_list[vert_id]
        if vert.val != vert.parent:
            vert.parent = self.get(vert.parent).parent
        return self.vert_list[vert.parent]

    def join(self, vert_id_1, vert_id_2):
        vert_1 = self.get(vert_id_1)
        vert_2 = self.get(vert_id_2)
        if vert_1.parent != vert_2.parent:
            if vert_2.count > vert_1.count:
                vert_1, vert_2 = vert_2, vert_1
            vert_2.parent = vert_1.parent
            vert_1.min = min(vert_1.min, vert_2.min)
            vert_1.max = max(vert_1.max, vert_2.max)
            vert_1.count += vert_2.count


_INPUT_LINES = sys.stdin.read().splitlines()
my_snm = SNM(int(_INPUT_LINES[0]))
for line in _INPUT_LINES[1:]:
    command, values = line.split(maxsplit=1)
    if command == 'union':
        id_1, id_2 = map(int, values.split())
        my_snm.join(id_1, id_2)
    elif command == 'get':
        vert = my_snm.get(int(values))
        print(vert.min, vert.max, vert.count)
    else:
        raise ValueError('unknown command')
