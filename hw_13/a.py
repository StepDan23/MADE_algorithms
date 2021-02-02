import sys


class Edge:
    def __init__(self, vert_id, capacity):
        self.vert_id = vert_id
        self.cap = capacity
        self.flow = 0
        self.back_edge = None

    def set_back_edge(self, edge):
        self.back_edge = edge


class Graph:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.list_of_edges = [[] for _ in range(n_vert)]
        self.used = None
        self.flow_size = -1  # init for +1 at start

    def add_edge(self, v_1, v_2, w):
        v_1, v_2 = v_1 - 1, v_2 - 1
        edge = Edge(v_2, w)
        back_edge = Edge(v_1, w)
        edge.set_back_edge(back_edge)
        back_edge.set_back_edge(edge)
        self.list_of_edges[v_1].append(edge)
        self.list_of_edges[v_2].append(back_edge)

    def _push_flow(self, vert_1, cur_flow):
        self.used[vert_1] = True
        last_vert = self.n_vert - 1
        if vert_1 == last_vert:
            return cur_flow
        for edge in self.list_of_edges[vert_1]:
            if not self.used[edge.vert_id] and edge.flow < edge.cap:
                next_flow = min(cur_flow, edge.cap - edge.flow)
                delta = self._push_flow(edge.vert_id, next_flow)
                if delta > 0:
                    edge.flow += delta
                    edge.back_edge.flow -= delta
                    return delta
        return 0

    def ford_fulkerson(self):
        delta = 1
        start_vert = 0
        while delta > 0:
            self.flow_size += delta
            self.used = [False for _ in range(n_vert)]
            delta = self._push_flow(start_vert, float('inf'))
        return self.flow_size


n_vert, _ = int(input()), input()
my_graph = Graph(n_vert)

for line in sys.stdin.read().splitlines():
    vert_1, vert_2, weight = map(int, line.split())
    my_graph.add_edge(vert_1, vert_2, weight)

print(my_graph.ford_fulkerson())
