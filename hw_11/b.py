import sys
import heapq


class Graph:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.list_of_edges = [[] for _ in range(n_vert)]
        self.dist = [float('inf') for _ in range(n_vert)]
        self.used = [False for _ in range(n_vert)]
        self.dist[0] = 0

    def add_edge(self, v_1, v_2, w):
        v_1, v_2 = v_1 - 1, v_2 - 1
        self.list_of_edges[v_1].append((v_2, w))
        self.list_of_edges[v_2].append((v_1, w))

    def dijkstra(self):
        h = []
        heapq.heappush(h, (0, 0))
        for _ in range(self.n_vert):
            _, next = heapq.heappop(h)
            while self.used[next]:
                _, next = heapq.heappop(h)
            self.used[next] = True
            for vert_edge, weight in self.list_of_edges[next]:
                if self.dist[vert_edge] > self.dist[next] + weight:
                    self.dist[vert_edge] = self.dist[next] + weight
                    heapq.heappush(h, (self.dist[vert_edge], vert_edge))


_INPUT_LINES = sys.stdin.buffer.read().decode().splitlines()
n_vert, n_edge = map(int, _INPUT_LINES[0].split())

my_graph = Graph(n_vert)
for line in _INPUT_LINES[1:]:
    vert_1, vert_2, weight = map(int, line.split())
    my_graph.add_edge(vert_1, vert_2, weight)

my_graph.dijkstra()
print(*my_graph.dist, sep=' ')

# входные данныеСкопировать
# 4 5
# 1 2 1
# 1 3 5
# 2 4 8
# 3 4 1
# 2 3 3
# выходные данныеСкопировать
# 0 1 4 5
