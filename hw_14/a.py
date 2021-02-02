import sys

_P = 83
_M = 1000001501


def init_arrays(word):
    word_len = len(word)
    hash_arr = [ord(word[0]) for _ in range(word_len)]
    pow_arr = [1 for _ in range(word_len)]
    for i in range(1, word_len):
        hash_arr[i] = (hash_arr[i - 1] * _P + ord(word[i])) % _M
        pow_arr[i] = (pow_arr[i - 1] * _P) % _M
    return hash_arr, pow_arr


def get_hash(left, right, hash_arr, pow_arr):
    if left == 0:
        return hash_arr[right]
    return (hash_arr[right] - hash_arr[left - 1] * pow_arr[right - left + 1]) % _M


input_word, _ = input(), input()
hashes, powers = init_arrays(input_word)

answer = []
for line in sys.stdin.read().splitlines():
    from_1, to_1, from_2, to_2 = map(lambda x: int(x) - 1, line.split())
    if (to_1 - from_1 == to_2 - from_2
            and get_hash(from_1, to_1, hashes, powers) == get_hash(from_2, to_2, hashes, powers)):
        answer.append('Yes')
    else:
        answer.append('No')
print(*answer, sep='\n')

