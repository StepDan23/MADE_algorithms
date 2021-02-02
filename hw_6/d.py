def levenshtein_dist(str_1, str_2):
    len_1, len_2 = len(str_1), len(str_2)
    if len_1 == 0 or len_2 == 0:
        return len_1 + len_2

    dp_matrix = [[i for i in range(len_1 + 1)] for _ in range(len_2 + 1)]
    for i in range(1, len_2 + 1):
        dp_matrix[i][0] = i
        for j in range(1, len_1 + 1):
            add_char = dp_matrix[i - 1][j] + 1
            del_char = dp_matrix[i][j - 1] + 1
            repl_char = dp_matrix[i - 1][j - 1] + (str_1[j - 1] != str_2[i - 1])
            dp_matrix[i][j] = min(add_char, del_char, repl_char)

    return dp_matrix[len_2][len_1]


inp_1 = input()
inp_2 = input()
if len(inp_1) > len(inp_2):
    inp_1, inp_2 = inp_2, inp_1
print(levenshtein_dist(inp_1, inp_2))

# входные данныеСкопировать
# ABCDEFGH
# ACDEXGIH
# выходные данныеСкопировать
# 3