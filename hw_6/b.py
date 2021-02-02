def make_route(mat, rows, cols):
    routes = []
    for i in range(rows):
        route = []
        for j in range(cols):
            if i == 0:
                route.append((i, j - 1))
                if j == 0:
                    continue
                mat[i][j] += mat[i][j - 1]
            elif j == 0:
                mat[i][j] += mat[i - 1][j]
                route.append((i - 1, j))
            else:
                left, top = mat[i][j - 1], mat[i - 1][j]
                if top > left:
                    mat[i][j] += top
                    route.append((i - 1, j))
                else:
                    mat[i][j] += left
                    route.append((i, j - 1))
        routes.append(route)
    return mat[-1][-1], routes


def restore_route(routes, rows, cols):
    i, j = rows - 1, cols - 1
    route = []
    while i > 0 or j > 0:
        if i == routes[i][j][0]:
            route.append('R')
        else:
            route.append('D')
        i, j = routes[i][j]
    return route[::-1]


x, y = map(int, input().split())
matrix = []
for _ in range(x):
    matrix.append(list(map(int, input().split())))
_reward, _routes = make_route(matrix, x, y)
_route = restore_route(_routes, x, y)
print(_reward)
print(*_route, sep='')

# входные данныеСкопировать
# 3 3
# 0 2 -3
# 2 -5 7
# 1 2 0
# выходные данныеСкопировать
# 6
# RRDD
matrix = []
x,y = 3, 3
matrix.append([0, 2, -3])
matrix.append([2, -5, 7])
matrix.append([1, 2, 0])
x,y = 2, 4
matrix.append([1, 31, 3, 513])
matrix.append([1000, 124, 2, 1])