def counter(arr):
    count_arr = [0] * (max(arr) + 1)
    for val in arr:
        count_arr[val] += 1
    return count_arr


def count_sort(arr):
    count_arr = counter(arr)
    sorted_arr = []
    for i, val in enumerate(count_arr):
        if val > 0:
            sorted_arr.extend([i] * val)
    return sorted_arr


a = [7, 3, 4, 2, 5, 5, 5, 7]
print(*count_sort(a))
assert count_sort(a) == [2, 3, 4, 5, 5, 5, 7, 7]
