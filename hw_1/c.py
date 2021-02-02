def merge(left, right):
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
    return arr


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    left, right = arr[:n // 2], arr[n // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


_ = input()
unordered_arr = list(map(int, input().split()))
print(*merge_sort(unordered_arr))
