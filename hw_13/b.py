import sys
from math import ceil, log2
from collections import deque


class Edge:
    def __init__(self, v_from, v_to, capacity):
        self.v_from = v_from
        self.v_to = v_to
        self.cap = capacity
        self.flow = 0
        self.back_edge = None

    def set_back_edge(self, edge):
        self.back_edge = edge


class Graph:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.list_of_edges = [[] for _ in range(n_vert)]
        self.all_edges = []
        self.used = None
        self.flow_size = 0
        self.max_weight = 0

    def add_edge(self, v_1, v_2, w):
        v_1, v_2 = v_1 - 1, v_2 - 1
        edge = Edge(v_1, v_2, w)
        back_edge = Edge(v_2, v_1, w)
        edge.set_back_edge(back_edge)
        back_edge.set_back_edge(edge)
        self.list_of_edges[v_1].append(edge)
        self.list_of_edges[v_2].append(back_edge)
        self.all_edges.append(edge)
        self.max_weight = max(self.max_weight, w)

    def bfs(self, start_vert, last_vert, delta):
        queue = deque([start_vert])
        cur_flow = float('inf')
        while queue:
            vert = queue.popleft()
            for edge in self.list_of_edges[vert]:
                if (self.used[edge.v_to] == -1
                        and delta <= edge.cap - edge.flow and edge.flow < edge.cap):
                    self.used[edge.v_to] = edge
                    cur_flow = min(cur_flow, edge.cap - edge.flow)
                    queue.append(edge.v_to)

                    if edge.v_to == last_vert:
                        return cur_flow
        return 0

    def edmonds_karp(self):
        start_vert = 0
        delta_arr = [2 ** val for val in range(ceil(log2(self.max_weight)), -1, -1)]
        for delta in delta_arr:
            cur_flow = 1
            while cur_flow:
                self.used = [-1 for _ in range(self.n_vert)]
                cur_flow = self.bfs(start_vert, self.n_vert - 1, delta)
                if cur_flow:
                    vert = self.n_vert - 1
                    while vert != start_vert:
                        u = self.used[vert]
                        u.flow += cur_flow
                        u.back_edge.flow -= cur_flow
                        vert = u.v_from
                self.flow_size += cur_flow
        return self.flow_size


n_vert, _ = int(input()), input()
my_graph = Graph(n_vert)

for line in sys.stdin.read().splitlines():
    vert_1, vert_2, weight = map(int, line.split())
    my_graph.add_edge(vert_1, vert_2, weight)

print(my_graph.edmonds_karp())
print(*[edge.flow for edge in my_graph.all_edges], sep='\n')
