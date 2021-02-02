import sys

_INF = 100_000


class Graph:
    def __init__(self, n_vert):
        self.n_vert = n_vert
        self.dist = []
        self.next = [[i for i in range(n_vert)] for _ in range(n_vert)]

    def floyd_circle(self):
        for k in range(self.n_vert):
            for u in range(self.n_vert):
                for v in range(self.n_vert):
                    if (self.dist[u][v] > self.dist[u][k] + self.dist[k][v]
                            and self.dist[u][k] < _INF
                            and self.dist[k][v] < _INF):
                        self.dist[u][v] = self.dist[u][k] + self.dist[k][v]
                        self.next[u][v] = self.next[u][k]
        circle_route = []
        for i in range(self.n_vert):
            if self.dist[i][i] < 0:
                circle_set = set()
                cur = self.next[i][i]
                while cur not in circle_set:
                    circle_route.append(cur + 1)
                    circle_set.add(cur)
                    cur = self.next[cur][cur]
                circle_route = circle_route[circle_route.index(cur + 1):]
                break
        return circle_route


_INPUT_LINES = sys.stdin.read().splitlines()
n_vert = int(_INPUT_LINES[0])
my_graph = Graph(n_vert)
for line in _INPUT_LINES[1:]:
    my_graph.dist.append(list(map(int, line.split())))

routes = my_graph.floyd_circle()
if len(routes) > 0:
    print('YES')
    print(len(routes))
    print(*routes, sep=' ')
else:
    print('NO')

# 4
# 0 1 0 0
# 0 0 2 0
# 0 -3 0 2
# 0 0 0 0

# входные данныеСкопировать
# 2
# 0 -1
# -1 0
# выходные данныеСкопировать
# YES
# 2
# 2 1
