from collections import deque


def make_step(x, y, n_max):
    steps = [(x + 1, y + 2), (x + 2, y + 1),
             (x + 2, y - 1), (x + 1, y - 2),
             (x - 1, y - 2), (x - 2, y - 1),
             (x - 2, y + 1), (x - 1, y + 2)]
    correct_steps = [(a, b) for (a, b) in steps
                     if 0 < a <= n_max and 0 < b <= n_max]
    return correct_steps


def bfs(start_vert, n_max):
    used = {start_vert: 0}
    queue = deque([start_vert])
    while queue:
        vert_x, vert_y = queue.popleft()
        for vert in make_step(vert_x, vert_y, n_max):
            if vert not in used:
                used[vert] = (vert_x, vert_y)
                queue.append(vert)
    return used


def recover_route(routes_dict, start, end):
    route = [end]
    vert = end
    while vert != start:
        vert = routes_dict[vert]
        route.append(vert)
    return route


n_max = int(input())
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

routes = bfs(start, n_max)
route = recover_route(routes, start, end)
print(len(route))
for vert in route[::-1]:
    print(*vert, sep=' ')

# входные данныеСкопировать
# 5
# 1 1
# 3 2
# выходные данныеСкопировать
# 2
# 1 1
# 3 2
