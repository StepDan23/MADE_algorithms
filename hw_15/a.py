class Lexer:
    def __init__(self, string):
        self.string = string
        self.cur_id = 0

    def next_token(self):
        token = self.string[self.cur_id]

        num = ''
        while token.isdigit():
            num += token
            self.cur_id += 1
            token = self.string[self.cur_id]

        if num:
            return int(num)

        self.cur_id += 1
        return token


inp = input()
lexer = Lexer(inp)
token = lexer.next_token()
while token != '.':
    print(token)
    token = lexer.next_token()
