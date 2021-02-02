import sys

NO_LETTER = 0
LETTER_EXISTS = 1
LETTER_TERMINAL = 2


class LetterNode:
    def __init__(self):
        self.is_terminal = NO_LETTER
        self.next = None


class Trie:
    def __init__(self):
        self.chars = [LetterNode() for _ in range(26)]

    @staticmethod
    def char_num(char):
        return ord(char) - ord('a')

    def insert(self, word, ind):
        word_list = self.chars
        for i in range(len(word)):
            char = self.char_num(word[i])
            if not word_list[char]:
                word_list[char] = LetterNode()
                word_list[char].is_terminal = LETTER_EXISTS
            if i == len(word) - 1:
                word_list[char].is_terminal = LETTER_TERMINAL + ind

            if not word_list[char].next:
                word_list[char].next = [LetterNode() for _ in range(26)]
            word_list = word_list[char].next

    def contains(self, word):
        word_list = self.chars
        for i in range(len(word) - 1):
            char = self.char_num(word[i])
            if not word_list[char] or not word_list[char].next:
                return NO_LETTER
            word_list = word_list[char].next
        return word_list[self.char_num(word[-1])].is_terminal


string, ans_len = input(), int(input())

my_trie = Trie()
for i, word in enumerate(sys.stdin.read().splitlines()):
    my_trie.insert(word, i)

answer = ['No' for _ in range(ans_len)]
for i in range(len(string)):
    for j in range(1, 31):
        if i + j > len(string):
            break
        else:
            sub_str = string[i: i + j]
            contains_ind = my_trie.contains(sub_str)
            if contains_ind >= LETTER_TERMINAL:
                answer[contains_ind - LETTER_TERMINAL] = 'Yes'

print(*answer, sep='\n')
