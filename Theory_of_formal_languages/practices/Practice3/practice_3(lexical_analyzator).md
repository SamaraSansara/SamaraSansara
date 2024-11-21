# Практическое занятие №3.

## Задание: 
Разработать программно-математическую модель распознавателя языка программирования. На выбранном ЯП реализовать простой лексический анализатор на базе конечного автомата.

lexical_analyzator.py:
```
class States:
    H = "H"
    ID = "ID"
    NUM = "NUM"
    OPER = "OPER"
    DELIM = "DELIM"
    COMM = "COMM"
    ERR = "ERR"


class TokNames:
    KWORD = "KWORD"
    IDENT = "IDENT"
    NUM = "NUM"
    OPER = "OPER"
    DELIM = "DELIM"
    COMMENT = "COMMENT"


class Token:
    def __init__(self, token_name, token_value):
        self.token_name = token_name
        self.token_value = token_value


class LexemeTable:
    def __init__(self, tok=None):
        self.tok = tok
        self.next = None


lt = None
lt_head = None

keywords = ["integer", "real", "boolean", "let", "if", "then", "else", "end_else", "for", "do", "while", "loop",
            "input", "output", "true", "false"]

group_operations = {
    "relation": ["NE", "EQ", "LT", "LE", "GT", "GE"],
    "addition": ["plus", "min", "or"],
    "multiplication": ["mult", "div", "and"],
    "unary": ["~"]
}

delimiters = ['(', ')', '{', '}', ';', ',', ':', '"']
bin_num = ['0', '1', 'B', 'b']
oct_num = ['0', '1', '2', '3', '4', '5', '6', '7', 'O', 'o']
dec_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 'd']
hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', 'H', 'h']
real_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', '.', '+', '-']


def add_token(tok):
    global lt, lt_head
    new_entry = LexemeTable(tok)
    if lt is None:
        lt = new_entry
        lt_head = new_entry
    else:
        lt.next = new_entry
        lt = new_entry


def is_kword(id):
    return id in keywords


def lexer(filename):
    try:
        with open(filename, "r") as fd:
            CS = States.H
            c = fd.read(1)
            while c:
                if CS == States.H:
                    while c in [' ', '\t', '\n']:
                        c = fd.read(1)
                    if c.isalpha() or c == '_':
                        CS = States.ID
                    elif c.isdigit() or c == '.':
                        CS = States.NUM
                    elif c in delimiters:
                        tok = Token(TokNames.DELIM, c)
                        add_token(tok)
                        c = fd.read(1)
                    elif c == '/':
                        c = fd.read(1)
                        if c == '*':
                            CS = States.COMM
                            c = fd.read(1)
                        else:
                            tok = Token(TokNames.OPER, "/")
                            add_token(tok)
                            CS = States.H
                    else:
                        CS = States.OPER
                elif CS == States.ID:
                    buf = c
                    c = fd.read(1)
                    while c.isalnum() or c == '_':
                        buf += c
                        c = fd.read(1)
                    if is_kword(buf):
                        tok = Token(TokNames.KWORD, buf)
                    else:
                        tok = Token(TokNames.IDENT, buf)
                    add_token(tok)
                    CS = States.H
                elif CS == States.NUM:
                    buf = ''
                    while c.isdigit() or c in real_num or c.isalpha():
                        buf += c
                        c = fd.read(1)
                    tok = Token(TokNames.NUM, buf)
                    add_token(tok)
                    CS = States.H
                elif CS == States.OPER:
                    buf = c
                    c = fd.read(1)
                    while buf in group_operations['relation'] or buf in group_operations['addition'] or buf in group_operations['multiplication']:
                        buf += c
                        c = fd.read(1)
                    tok = Token(TokNames.OPER, buf.strip())
                    add_token(tok)
                    CS = States.H
                elif CS == States.COMM:
                    while c:
                        if c == '*':
                            c = fd.read(1)
                            if c == '/':
                                CS = States.H
                                c = fd.read(1)
                                break
                        c = fd.read(1)
                elif CS == States.ERR:
                    print(f"Error: Unexpected character {c}")
                    CS = States.H

    except FileNotFoundError:
        print(f"Cannot open file {filename}.")
        return -1


def print_tokens(lt_head):
    current = lt_head
    while current:
        print(f"Token Name: {current.tok.token_name}, Token Value: {current.tok.token_value}")
        current = current.next


def main():
    filename = "test_lexical_analyzator.txt"
    result = lexer(filename)
    if result == -1:
        print("Lexical analysis failed.")
    else:
        print("Lexical analysis successful.")
        print_tokens(lt_head)


if __name__ == "__main__":
    main()


```

test_lexical_analyzator.txt:

```
int a, b
begin
while (a = 1):
    a:=61e+2;
    writeln a;
end(*Комментарий*)
```


## Результат: 
```
Lexical analysis successful.
Token Name: IDENT, Token Value: int
Token Name: IDENT, Token Value: a
Token Name: DELIM, Token Value: ,
Token Name: IDENT, Token Value: b
Token Name: IDENT, Token Value: begin
Token Name: KWORD, Token Value: while
Token Name: DELIM, Token Value: (
Token Name: IDENT, Token Value: a
Token Name: OPER, Token Value: =
Token Name: NUM, Token Value: 1
Token Name: DELIM, Token Value: )
Token Name: DELIM, Token Value: :
Token Name: IDENT, Token Value: a
Token Name: DELIM, Token Value: :
Token Name: OPER, Token Value: =
Token Name: NUM, Token Value: 61e+2
Token Name: DELIM, Token Value: ;
Token Name: IDENT, Token Value: writeln
Token Name: IDENT, Token Value: a
Token Name: DELIM, Token Value: ;
Token Name: IDENT, Token Value: end
Token Name: DELIM, Token Value: (
Token Name: OPER, Token Value: *
Token Name: IDENT, Token Value: Комментарий
Token Name: OPER, Token Value: *
Token Name: DELIM, Token Value: )

```

<img width="763" alt="Screenshot 2024-11-21 at 04 00 38" src="https://github.com/user-attachments/assets/410b6947-5342-44ae-a43a-e7a73cd58e28">

<img width="755" alt="Screenshot 2024-11-21 at 04 00 50" src="https://github.com/user-attachments/assets/7b740a73-827f-497d-aa2b-fb8c06c5f391">

Открываем терминал:

<img width="767" alt="Screenshot 2024-11-21 at 04 01 21" src="https://github.com/user-attachments/assets/5595baa4-0169-49b8-bcd9-4be7dab14c66">
