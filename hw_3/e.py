def check_copies(speed_1, speed_2, total_time, n_copies):
    total_copies = total_time // speed_1 + total_time // speed_2
    if total_copies >= n_copies:
        return True
    return False


def find_time(speed_1, speed_2, n_copies):
    left = -1
    right = n_copies * speed_1
    while left < right - 1:
        mid = (right + left) // 2
        if check_copies(speed_1, speed_2, mid, n_copies):
            right = mid
        else:
            left = mid
    return right


need_copies, speed_one, speed_two = map(int, input().split())
if speed_one > speed_two:
    speed_one, speed_two = speed_two, speed_one
print(find_time(speed_one, speed_two, need_copies - 1) + speed_one)

# входные данныеСкопировать
# 4 1 1
# выходные данныеСкопировать
# 3
# входные данныеСкопировать
# 5 1 2
# выходные данныеСкопировать
# 4