from random import choice


def partition(arr, pivot):
    less, equal, greater = [], [], []
    for val in arr:
        if val < pivot:
            less.append(val)
        elif val > pivot:
            greater.append(val)
        else:
            equal.append(val)
    return less, equal, greater


def q_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choice(arr)
    less, equal, greater = partition(arr, pivot)
    less = q_sort(less)
    greater = q_sort(greater)
    return less + equal + greater


_ = input()
unordered_arr = list(map(int, input().split()))
print(*q_sort(unordered_arr))
