import sys
import threading

sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)

_DEFAULT_COLOR = 0


class Graph:
    def __init__(self, n_vert):
        self.list_of_edges = [set() for _ in range(n_vert)]
        self.colors = [_DEFAULT_COLOR for _ in range(n_vert)]

    def add_edge(self, v_1, v_2):
        v_1, v_2 = v_1 - 1, v_2 - 1
        self.list_of_edges[v_1].add(v_2)
        self.list_of_edges[v_2].add(v_1)

    def dfs(self, vert, cur_color):
        self.colors[vert] = cur_color
        for vert_edge in self.list_of_edges[vert]:
            if self.colors[vert_edge] == _DEFAULT_COLOR:
                self.dfs(vert_edge, cur_color)


def main():
    _INPUT_LINES = sys.stdin.read().splitlines()
    n_vert, n_edges = map(int, _INPUT_LINES[0].split())
    my_graph = Graph(n_vert)
    cur_color = _DEFAULT_COLOR
    for line in _INPUT_LINES[1:]:
        vert_1, vert_2 = map(int, line.split())
        my_graph.add_edge(vert_1, vert_2)

    for vert_id in range(n_vert):
        if my_graph.colors[vert_id] == _DEFAULT_COLOR:
            cur_color += 1
            my_graph.dfs(vert_id, cur_color)
    print(len(set(my_graph.colors)))
    print(' '.join(map(str, my_graph.colors)))


if __name__ == "__main__":
    threading.Thread(target=main).start()