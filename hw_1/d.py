def merge(left, right):
    global N_swaps
    m = len(left) + len(right)
    i, j = 0, 0
    arr = []
    while i + j < m:
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
            N_swaps += len(left) - i
    return arr


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    left, right = arr[:n // 2], arr[n // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


N_swaps = 0
_ = input()
unordered_arr = list(map(int, input().split()))
merge_sort(unordered_arr)
print(N_swaps)
