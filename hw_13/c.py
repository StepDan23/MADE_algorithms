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


n_vert, n_edges = map(int, input().split())
# n_vert = 3
# n_edges = 3
my_graph = Graph(n_vert)

_inp = sys.stdin.read().splitlines()
# _inp = ['1 2 3', '1 3 5', '3 2 7']
# for line in sys.stdin.read().splitlines():
for line in _inp:
    vert_1, vert_2, weight = map(int, line.split())
    my_graph.add_edge(vert_1, vert_2, weight)

flow = my_graph.edmonds_karp()

start_vert = 0
start_set = set()
queue = deque([start_vert])
while queue:
    vert = queue.popleft()
    start_set.add(vert)
    for edge in my_graph.list_of_edges[vert]:
        if edge.back_edge.flow > 0 and edge.back_edge.flow:
            queue.append(edge.v_to)

ans = []
sum_flow = 0
for edge_id in range(n_edges):
    edge = my_graph.all_edges[edge_id]
    if edge.v_from in start_set and edge.v_to not in start_set:
        sum_flow += my_graph.all_edges[edge_id].cap
        ans.append(edge_id + 1)

if sum_flow > flow:
    raise ValueError('123')

print(len(ans), sum_flow)
print(*ans, sep=' ')

# входные данныеСкопировать
# 3 3
# 1 2 3
# 1 3 5
# 3 2 7
# выходные данныеСкопировать
# 2 8
# 1 2
