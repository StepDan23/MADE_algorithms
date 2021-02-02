def counter(arr):
    count_arr = [0] * 26
    for letter in arr:
        count_arr[ord(letter) - ord('a')] += 1
    return count_arr


def check_possible(sub_arr, cards_arr):
    for i in range(len(sub_arr)):
        if sub_arr[i] > cards_arr[i]:
            return 0
    return 1


def count_sub_arrays(arr, cards_arr):
    total = 0
    left, right = 0, 1
    sub_arr = [0] * 26
    first_char_id = ord(arr[0]) - ord('a')
    sub_arr[first_char_id] = 1
    while left < len(arr) or right < len(arr):
        if check_possible(sub_arr, cards_arr):
            total += right - left
            if right == len(arr):
                return total
            right_char_id = ord(arr[right]) - ord('a')
            sub_arr[right_char_id] += 1
            right += 1
        else:
            left_char_id = ord(arr[left]) - ord('a')
            sub_arr[left_char_id] -= 1
            left += 1
    return total


_, word_1, word_2 = input(), input(), input()
print(count_sub_arrays(word_1, counter(word_2)))


word_1 = 'abacaba'
word_2 = 'abc'
print(count_sub_arrays(word_1, counter(word_2)))
