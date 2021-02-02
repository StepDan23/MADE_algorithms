def first_positive(arr):
    """ Return first positive or maximum of negative value """
    max_ind = 0
    i = 0
    while i < len(arr):
        if arr[i] >= 0:
            return i
        if arr[i] > arr[max_ind]:
            max_ind = i
        i += 1
    return max_ind


def make_route(rewards_arr, size):
    price = 0
    route = [1]
    i = 0
    while i < len(rewards_arr):
        arr_slice = rewards_arr[i:(i + size)]
        ind = first_positive(arr_slice)
        price += arr_slice[ind]
        i = i + ind + 1
        route.append(i + 1)
    return price, route


_, jump_len = map(int, input().split())
rewards = list(map(int, input().split()))
rewards.append(0)
max_price, top_route = make_route(rewards, jump_len)
print(max_price)
print(len(top_route) - 1)
print(*top_route, sep=' ')

# входные данныеСкопировать
# 5 3
# 2 -3 5
# выходные данныеСкопировать
# 7
# 3
# 1 2 4 5
