def z_function(word):
    left, right = 0, 0
    word_len = len(word)
    z_values = [0 for _ in range(word_len)]
    for i in range(1, word_len):
        z_values[i] = max(0, min(right - i, z_values[i - left]))
        while (i + z_values[i] < word_len
               and word[z_values[i]] == word[i + z_values[i]]):
            z_values[i] += 1
        if i + z_values[i] > right:
            left = i
            right = i + z_values[i]
    return z_values


z_values_list = z_function(input())
print(*z_values_list[1:], sep=' ')

# входные данныеСкопировать
# aaaAAA
# выходные данныеСкопировать
#  2 1 0 0 0
# входные данныеСкопировать
# abacaba
# выходные данныеСкопировать
#  0 1 0 3 0 1
