import sys


def lower_bound(arr, x):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (right + left) // 2
        if x <= arr[mid]:
            right = mid
        else:
            left = mid
    return right


_INPUT_LINES = sys.stdin.read().splitlines()
inp_arr = sorted(list(map(int, _INPUT_LINES[1].split())))

output = [0] * int(_INPUT_LINES[2])
for i, line in enumerate(_INPUT_LINES[3:]):
    left_val, right_val = map(int, line.split())
    lower_b = lower_bound(inp_arr, left_val)
    upper_b = lower_bound(inp_arr, right_val + 1)
    output[i] = upper_b - lower_b

sys.stdout.write("\n".join(map(str, output)))
