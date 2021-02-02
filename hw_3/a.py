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


_, _ = input().split()
inp_arr = list(map(int, input().split()))
values = list(map(int, input().split()))

for val in values:
    lower_ind = lower_bound(inp_arr, val)
    if lower_ind == 0:
        print(inp_arr[0])
    elif lower_ind == len(inp_arr):
        print(inp_arr[-1])
    else:
        output_ind = lower_ind - 1 if val - inp_arr[lower_ind - 1] <= inp_arr[lower_ind] - val else lower_ind
        print(inp_arr[output_ind])