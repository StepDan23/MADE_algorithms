from math import log2, ceil


n, m, a_0 = map(int, input().split())
u, v = map(int, input().split())


def next_u(prev_u, prev_ans, i):
    return (17 * prev_u + 751 + prev_ans + 2 * i) % n + 1


def next_v(prev_v, prev_ans, i):
    return (13 * prev_v + 593 + prev_ans + 5 * i) % n + 1


def next_a(prev_a):
    return (23 * prev_a + 21563) % 16714589


def rmq_matrix(arr):
    mat = [[0 for _ in range(ceil(log2(n)) + 1)] for _ in range(n)]
    for left in range(n - 1, -1, -1):
        mat[left][0] = arr[left]
        for k in range(ceil(log2(n))):
            prev_ind = min(left + (1 << k), n - 1)
            mat[left][k + 1] = min(mat[left][k], mat[prev_ind][k])
    return mat


arr = [0 for _ in range(n)]
arr[0] = a_0
for i in range(1, n):
    arr[i] = next_a(arr[i - 1])

logs = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    logs[i] = logs[i // 2] + 1

matrix = rmq_matrix(arr)


def rmq(left, right):
    k = logs[right - left + 1]
    return min(matrix[left][k],
               matrix[right - (1 << k) + 1][k])


ans = rmq(*sorted([u - 1, v - 1]))
for i in range(1, m):
    u = next_u(u, ans, i)
    v = next_v(v, ans, i)
    if u > v:
        ans = rmq(v - 1, u - 1)
    else:
        ans = rmq(u - 1, v - 1)
print(u, v, ans)


# входные данныеСкопировать
# 10 8 12345
# 3 9
# выходные данныеСкопировать
# 5 3 1565158
