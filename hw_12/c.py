import sys
import math


class Graph:
    def __init__(self, n_vert, matrix):
        self.n_vert = n_vert
        self.vertexes_coords = matrix
        self.dist = [float('inf') for _ in range(n_vert)]
        self.dist[0] = 0
        self.used = [False for _ in range(n_vert)]
        self.distance = 0

    def _vert_dist(self, ind_from, ind_to):
        if ind_to == ind_from:
            return float('inf')
        x_1 = self.vertexes_coords[ind_from][0]
        y_1 = self.vertexes_coords[ind_from][1]
        x_2 = self.vertexes_coords[ind_to][0]
        y_2 = self.vertexes_coords[ind_to][1]
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def dijkstra(self):
        for _ in range(self.n_vert):
            next = -1
            for vert_id in range(self.n_vert):
                if ((not self.used[vert_id])
                        and (next == -1 or self.dist[vert_id] < self.dist[next])):
                    next = vert_id
            if self.dist[next] == float('inf'):
                break
            self.used[next] = True
            if self.dist[next] != float('inf'):
                self.distance += self.dist[next]
            for vert_edge in range(self.n_vert):
                weight = self._vert_dist(next, vert_edge)
                self.dist[vert_edge] = min(self.dist[vert_edge], weight)


n_vert = int(input())
vertexes = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
my_graph = Graph(n_vert, vertexes)
my_graph.dijkstra()
print(my_graph.distance)
