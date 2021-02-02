import sys
import threading
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)


class Graph:
    def __init__(self, n_vert):
        self.list_of_edges = defaultdict(set)
        self.t_in = [0 for _ in range(n_vert)]
        self.up = [0 for _ in range(n_vert)]
        self.single_points = set()

    def add_edge(self, v_1, v_2):
        v_1, v_2 = v_1 - 1, v_2 - 1
        self.list_of_edges[v_2].add(v_1)
        self.list_of_edges[v_1].add(v_2)

    def dfs(self, vert, cur_time):
        cur_time += 1
        n_child = 0
        self.t_in[vert] = cur_time
        self.up[vert] = cur_time
        for vert_edge in self.list_of_edges[vert]:
            if self.t_in[vert_edge] == 0:
                n_child += 1
                self.dfs(vert_edge, cur_time)
                self.up[vert] = min(self.up[vert], self.up[vert_edge])
                if (self.up[vert_edge] >= self.t_in[vert]) & (cur_time != 1):
                    self.single_points.add(vert + 1)
            else:
                self.up[vert] = min(self.up[vert], self.t_in[vert_edge])

        # root
        if (cur_time == 1) & (n_child >= 2):
            self.single_points.add(vert + 1)


def main():
    _INPUT_LINES = sys.stdin.read().splitlines()
    n_vert, n_edges = map(int, _INPUT_LINES[0].split())
    my_graph = Graph(n_vert)
    for line in _INPUT_LINES[1:]:
        vert_1, vert_2 = map(int, line.split())
        my_graph.add_edge(vert_1, vert_2)

    for vert in range(n_vert):
        if my_graph.t_in[vert] == 0:
            my_graph.dfs(vert, 0)

    print(len(my_graph.single_points))
    print(*sorted(my_graph.single_points), sep=' ')


if __name__ == "__main__":
    threading.Thread(target=main).start()
