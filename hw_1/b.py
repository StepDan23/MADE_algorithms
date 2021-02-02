def bubble_sort(arr):
    for i in range(len(arr)):
        ind_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[ind_min]:
                ind_min = j
        arr[ind_min], arr[i] = arr[i], arr[ind_min]  # swap
    return arr


_ = input()
arr = list(map(int, input().split()))
print(*bubble_sort(arr))


print(*bubble_sort([1, 8, 2, 1, 4, 7, 3, 2, 3, 6]))