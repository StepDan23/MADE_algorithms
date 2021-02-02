from math import sqrt

_EPS = 1e-5
_MIN_X = 0.0
_MAX_X = 1.0


def time_to_end(speed_1, speed_2, x_split, y_split):
    field_time = sqrt(x_split ** 2 + (1 - y_split) ** 2) / speed_1
    forest_time = sqrt((1 - x_split) ** 2 + y_split ** 2) / speed_2
    return field_time + forest_time


def find_point(speed_1, speed_2, split_l):
    left, right = _MIN_X, _MAX_X
    while abs(left - right) > _EPS:
        mid_1 = left + (right - left) / 3
        mid_2 = left + 2 * (right - left) / 3
        if time_to_end(speed_1, speed_2, mid_1, split_l) > time_to_end(speed_1, speed_2, mid_2, split_l):
            left = mid_1
        else:
            right = mid_2
    return right


speed_field, speed_forest = map(int, input().split())
split_line = float(input())
print(find_point(speed_field, speed_forest, split_line))


# входные данныеСкопировать
# 5 3
# 0.4
# выходные данныеСкопировать
# 0.783310604