def digital_sort(list_arr, index):

    index = len(list_arr[0]) - index - 1
    count_arr = [[] for _ in range(26)]
    for word in list_arr:
        insert_index = ord(word[index]) - ord('a')
        count_arr[insert_index].append(word)

    sorted_list = []
    for list_words in count_arr:
        if list_words:
            sorted_list.extend(list_words)

    return sorted_list


n_rows, _, n_iter = map(int, input().split())
input_arr = []
for _ in range(n_rows):
    input_arr.append(input())

for i in range(n_iter):
    input_arr = digital_sort(input_arr, i)

print(*input_arr, sep='\n')
