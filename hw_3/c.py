from math import sqrt

_EPS = 1e-7
_MIN_X = 0
_MAX_X = 1e5


def custom_func(x):
    return sqrt(x) + x ** 2


def find_zero(c_val):
    left, right = _MIN_X, _MAX_X
    mid = (left + right) / 2
    func_val = custom_func(mid)
    while abs(func_val - c_val) > _EPS:
        mid = (left + right) / 2
        func_val = custom_func(mid)
        if func_val > c_val:
            right = mid
        else:
            left = mid
    return mid


c = float(input())
print(find_zero(c))