import sys
import threading

sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)

_DEFAULT_COLOR = 0
_GREY = 1
_BLACK = 2


class Graph:
    def __init__(self, n_vert):
        self.list_of_edges = [[] for _ in range(n_vert)]
        self.colors = [_DEFAULT_COLOR for _ in range(n_vert)]
        self.route = []
        self.have_circle = False

    def add_edge(self, v_1, v_2):
        v_1, v_2 = v_1 - 1, v_2 - 1
        self.list_of_edges[v_1].append(v_2)

    def dfs(self, vert):
        for vert_edge in self.list_of_edges[vert]:
            if self.colors[vert_edge] == _DEFAULT_COLOR:
                self.colors[vert_edge] = _GREY
                self.dfs(vert_edge)
            elif self.colors[vert_edge] == _GREY:
                self.have_circle = True
        self.route.append(vert + 1)
        self.colors[vert] = _BLACK


def main():
    _INPUT_LINES = sys.stdin.read().splitlines()
    n_vert, n_edges = map(int, _INPUT_LINES[0].split())
    my_graph = Graph(n_vert)

    for line in _INPUT_LINES[1:]:
        vert_1, vert_2 = map(int, line.split())
        my_graph.add_edge(vert_1, vert_2)

    for vert_id in range(n_vert):
        if my_graph.colors[vert_id] == _DEFAULT_COLOR:
            my_graph.dfs(vert_id)

    if my_graph.have_circle:
        print(-1)
    else:
        print(*my_graph.route[::-1], sep=' ')


if __name__ == "__main__":
    threading.Thread(target=main).start()
