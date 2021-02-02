import sys
import threading

sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)

_DEFAULT_COLOR = 0
_VISITED = 1


class Graph:
    def __init__(self, n_vert):
        self.list_of_edges = [[] for _ in range(n_vert)]
        self.colors = [_DEFAULT_COLOR for _ in range(n_vert)]
        self.route = []

    def add_edge(self, v_1, v_2):
        v_1, v_2 = v_1 - 1, v_2 - 1
        self.list_of_edges[v_1].append(v_2)

    def dfs(self, vert, color_id):
        self.colors[vert] = color_id
        for vert_edge in self.list_of_edges[vert]:
            if self.colors[vert_edge] == _DEFAULT_COLOR:
                self.dfs(vert_edge, color_id)
        self.route.append(vert)


def main():
    _INPUT_LINES = sys.stdin.read().splitlines()
    n_vert, n_edges = map(int, _INPUT_LINES[0].split())
    forward_graph = Graph(n_vert)
    backward_graph = Graph(n_vert)
    for line in _INPUT_LINES[1:]:
        vert_1, vert_2 = map(int, line.split())
        forward_graph.add_edge(vert_1, vert_2)
        backward_graph.add_edge(vert_2, vert_1)

    # Топологическая сортировка
    for vert_id in range(n_vert):
        if forward_graph.colors[vert_id] == _DEFAULT_COLOR:
            forward_graph.dfs(vert_id, _VISITED)

    # Компоненты связанности
    cur_color = _DEFAULT_COLOR
    for vert_id in forward_graph.route[::-1]:
        if backward_graph.colors[vert_id] == _DEFAULT_COLOR:
            cur_color += 1
            backward_graph.dfs(vert_id, cur_color)

    # Новые пути
    new_routes = set()
    for vert_id in range(n_vert):
        for edge_id in forward_graph.list_of_edges[vert_id]:
            new_vert_1, new_vert_2 = backward_graph.colors[vert_id], backward_graph.colors[edge_id]
            if new_vert_1 != new_vert_2:
                new_routes.add(f'{new_vert_1}_{new_vert_2}')
    print(len(new_routes))


if __name__ == "__main__":
    threading.Thread(target=main).start()
