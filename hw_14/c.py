def p_function(word):
    word_len = len(word)
    p_values = [0 for _ in range(word_len)]
    for i in range(1, word_len):
        k = p_values[i - 1]
        while k > 0 and word[i] != word[k]:
            k = p_values[k - 1]
        if word[i] == word[k]:
            k += 1
        p_values[i] = k
    return p_values


def kmp(word, string):
    kmp_string = word + '#' + string
    p_values = p_function(kmp_string)
    indices = [ind - 2 * len(word) + 1 for ind in range(len(kmp_string)) if p_values[ind] == len(word)]
    return indices


inp_word = input()
inp_string = input()
answer = kmp(inp_word, inp_string)
print(len(answer))
print(*answer, sep=' ')
