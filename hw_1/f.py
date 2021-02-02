NUMBERS = ((50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def convert_text(s):
    num = 0
    for val, text in NUMBERS:
        len_t = len(text)
        while s[:len_t] == text:
            num += val
            s = s[len_t:]
    return num


in_arr = []
for _ in range(int(input())):
    in_arr.append(input().split())
print(*[' '.join(arr) for arr in sorted(in_arr, key=lambda x: (x[0], convert_text(x[1])))], sep='\n')

