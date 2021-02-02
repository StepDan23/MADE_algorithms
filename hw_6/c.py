def argmax(arr):
    max_ind, i = 0, 0
    while i < len(arr):
        if arr[i] > arr[max_ind]:
            max_ind = i
        i += 1
    return max_ind


def argmax_count(arr, cur_ind, count_arr):
    max_ind = cur_ind
    cur_val = arr[cur_ind]
    max_count, i = 0, 0
    while i < cur_ind:
        if arr[i] < cur_val and count_arr[i] > max_count:
            max_count = count_arr[i]
            max_ind = i
        i += 1
    return max_ind


def make_routes(arr):
    routes = [0 for _ in range(len(arr))]
    count_arr = [0 for _ in range(len(arr))]
    i = 0
    while i < len(arr):
        ind = argmax_count(arr, i, count_arr)
        routes[i] = ind
        count_arr[i] = count_arr[ind] + 1
        i += 1
    return routes, count_arr


def restore_route(arr, count_arr, routes):
    cur_ind = argmax(count_arr)
    ans = [arr[cur_ind]]
    while count_arr[cur_ind] != 1:
        cur_ind = routes[cur_ind]
        ans.append(arr[cur_ind])
    return ans[::-1]


_ = int(input())
num_arr = list(map(int, input().split()))
routes_arr, cnt_arr = make_routes(num_arr)
ans_arr = restore_route(num_arr, cnt_arr, routes_arr)
print(len(ans_arr))
print(*ans_arr)

# входные данныеСкопировать
# 8
# 1 4 1 5 3 3 4 2
# выходные данныеСкопировать
# 3
# 1 4 5

# входные данныеСкопировать
# 3
# 1 2 3
# выходные данныеСкопировать
# 3
# 1 2 3
