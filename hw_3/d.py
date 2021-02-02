import sys

_MIN_LENGTH = 0
_MAX_LENGTH = int(1e7 + 1)


def check_possible(arr, n_houses, length):
    variants = 0
    for val in arr:
        variants += val // length
    return variants >= n_houses


def find_length(arr, n_houses):
    left, right = _MIN_LENGTH, _MAX_LENGTH
    while left < right - 1:
        mid = (left + right) // 2
        if check_possible(arr, n_houses, mid):
            left = mid
        else:
            right = mid
    return left


_INPUT_LINES = sys.stdin.read().splitlines()
_, num_houses = map(int, _INPUT_LINES[0].split())
arr_ropes = list(map(int, _INPUT_LINES[1:]))
print(find_length(arr_ropes, num_houses))

#
# 4 11
# 802
# 743
# 457
# 539