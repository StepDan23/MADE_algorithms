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


class Graph:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.edges = []
        self.snm = SNM(n_vert)
        self.min_weight = 0

    def add_edge(self, v_1, v_2, w):
        self.edges.append((v_1, v_2, w))
        self.edges.append((v_2, v_1, w))

    def kruskal(self):
        edges = sorted(self.edges, key=lambda x: x[2])
        for v_1, v_2, w in edges:
            if self.snm.get(v_1) != self.snm.get(v_2):
                self.snm.join(v_1, v_2)
                self.min_weight += w


n_vert, n_edge = map(int, input().split())
my_graph = Graph(n_vert)
for line in sys.stdin.read().splitlines():
    vert_1, vert_2, weight = map(int, line.split())
    my_graph.add_edge(vert_1, vert_2, weight)
my_graph.kruskal()
print(my_graph.min_weight)
