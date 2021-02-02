import operator as op


class Lexer:
    def __init__(self, string):
        self.string = string
        self.cur_id = 0
        self.vars = {'Ded Moroz': 2020,
                     'Moroz': -30,
                     'Snegurochka': 10,
                     'Podarok': 'pod'}

    def next_token(self):
        token = self.string[self.cur_id]

        while token.isspace():
            self.cur_id += 1
            token = self.string[self.cur_id]

        var = ''
        while token.isalpha():
            var += token
            self.cur_id += 1
            token = self.string[self.cur_id]
        if var:
            return self.vars[var]

        num = ''
        while token.isdigit():
            num += token
            self.cur_id += 1
            token = self.string[self.cur_id]
        if num:
            return int(num)

        self.cur_id += 1
        return token


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = self.lexer.next_token()
        self.ops = {
            '-': op.sub,
            '+': op.add,
            'pod': lambda x: x+5
        }

    def parse_factor(self):
        if self.token == '(':
            self.token = self.lexer.next_token()
            if self.token in ['-', '+', '*', ')']:
                raise ValueError
            sum = self.parse_sum()
            self.token = self.lexer.next_token()
            if self.token not in ['-', '+', '*', ')', '.', 'pod']:
                raise ValueError
            return sum
        else:
            num = self.token
            self.token = self.lexer.next_token()
            return num

    def parse_sum(self):
        prod_1 = self.parse_prod()
        while self.token in ['+', '-', 'pod']:
            opp = self.ops[self.token]
            self.token = self.lexer.next_token()
            prod_2 = self.parse_prod()
            prod_1 = opp(prod_1, prod_2)
        return prod_1

    def parse_prod(self):
        fact_1 = self.parse_factor()
        while self.token == '*':
            self.token = self.lexer.next_token()
            fact_2 = self.parse_factor()
            fact_1 *= fact_2
        return fact_1


inp = input()
inp = 'Podarok(Moroz-Ded Moroz)*2.'
try:
    parser = Parser(Lexer(inp))
    result = int(parser.parse_sum())
    if parser.token != '.':
        raise ValueError
    print(result)
except:
    print('WRONG')
