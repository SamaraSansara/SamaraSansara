# Практическое занятие №3. Конфигурационные языки

П.Н. Советов, РТУ МИРЭА

Разобраться, что собой представляют программируемые конфигурационные языки (Jsonnet, Dhall, CUE).

  ## Задача 1

Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

Решение:

```

local groupPrefix = "ИКБО-";
local groupSuffix = "-20";

local groups = [groupPrefix + x + groupSuffix for x in std.range(1, 24)];

local students = [
  { age: 19, group: groupPrefix + "4" + groupSuffix, name: "Иванов И.И." },
  { age: 18, group: groupPrefix + "5" + groupSuffix, name: "Петров П.П." },
  { age: 18, group: groupPrefix + "5" + groupSuffix, name: "Сидоров С.С." },
  { age: 19, group: groupPrefix + "1" + groupSuffix, name: "Уджуху В.Т." }
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление"
}

```
<img width="522" alt="Screenshot 2024-10-18 at 19 38 47" src="https://github.com/user-attachments/assets/7cfef0f3-d214-4ace-a13a-f342bb98964f">

<img width="527" alt="Screenshot 2024-10-18 at 19 39 03" src="https://github.com/user-attachments/assets/9b458477-c66a-44d4-9c3d-74db29b364b5">


<img width="523" alt="Screenshot 2024-10-18 at 19 39 25" src="https://github.com/user-attachments/assets/ad63fdbf-ffa4-4597-a4b2-c5515e064d44">


## Задача 2

Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    <добавьте ваши данные в качестве четвертого студента>
  ],
  "subject": "Конфигурационное управление"
} 
```


Решение: 

```
let List/map = https://prelude.dhall-lang.org/List/map
let List/generate = https://prelude.dhall-lang.org/v15.0.0/List/generate

let groups = List/generate 24 Text (\(n : Natural) -> "ИКБО-${Natural/show (n + 1)}-20")

let Student = {age: Natural, group: Text, name: Text}

let students : List Student = 
[ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }, 
  { age = 18, group = "ИКБО-5-20", name = "Петров П.П." },
  { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." },
  { age = 19, group = "ИКБО-10-23", name = "Уджуху В.Т." }
]

let subject : Text = "Конфигурационное управление"

in {groups = groups, students = students, subject = subject}
```
<img width="345" alt="Screenshot 2024-10-20 at 15 05 35" src="https://github.com/user-attachments/assets/0d7c6baa-4cf1-4ace-b84e-96dca7364e2d">



<img width="350" alt="Screenshot 2024-10-20 at 15 05 48" src="https://github.com/user-attachments/assets/65e76a60-8658-4cc4-a57e-735d4b948b00">



<img width="364" alt="Screenshot 2024-10-20 at 15 06 07" src="https://github.com/user-attachments/assets/81bcadd9-d913-4bd2-a898-b8d86171c906">


<img width="472" alt="Screenshot 2024-10-20 at 16 50 33" src="https://github.com/user-attachments/assets/e38dd8d8-e4d1-4041-b0ab-79e4621d218f">



Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:

## Задача 3

Язык нулей и единиц.

```
10
100
11
101101
000
```
Решение: 

```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('::=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
<start> ::= <sequence>
<sequence> ::= "0" | "1" | "00" | "11" | "10" | "100" | "101101" | <sequence> "0" | <sequence> "1"
'''

print("10\n100\n11\n101101\n000\n")

grammar = parse_bnf(BNF)
for i in range(10):
    print(generate_phrase(grammar, '<start>'))

```

<img width="97" alt="Screenshot 2024-10-20 at 18 29 46" src="https://github.com/user-attachments/assets/8f30560d-21e2-4c66-aca4-e749c1ad6cdc">



## Задача 4

Язык правильно расставленных скобок двух видов.

```
(({((()))}))
{}
{()}
()
{}
```

Решение: 


```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('::=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
<start> ::= <brackets>
<brackets> ::= <round> | <curly> | <round> <brackets> | <curly> <brackets>
<round> ::= "(" <brackets> ")" | "()"
<curly> ::= "{" <brackets> "}" | "{}"
'''
print("(({((()))}))\n{}\n{()}\n()\n{}\n")

grammar = parse_bnf(BNF)
for i in range(10):
    print(generate_phrase(grammar, '<start>'))

```
<img width="850" alt="Screenshot 2024-10-20 at 18 40 03" src="https://github.com/user-attachments/assets/40afe46c-9a1a-407a-8fab-691c75f3b365">


## Задача 5

Язык выражений алгебры логики.

```
((~(y & x)) | (y) & ~x | ~x) & x
y & ~(y)
(~(y) & y & ~y)
~x
~((x) & y | (y) | (x)) & x | x | (y & ~y)
```


Решение: 

```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('::=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start, max_depth=10, depth=0):
    if depth > max_depth:
        return random.choice(["x", "y"])  
    
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name, max_depth, depth + 1) for name in seq])
    
    return str(start)

BNF = '''
<start> ::= <expression>
<expression> ::= <term> | <expression> "|" <term> | <expression> "&" <term>
<term> ::= <factor> | <term> "&" <factor> | <term> "|" <factor>
<factor> ::= <variable> | "~" <factor> | <term>
<variable> ::= x | y
'''

print("Реализовать грамматики, описывающие язык выражений алгебры логики.\n")

grammar = parse_bnf(BNF)
for i in range(10):
    print(generate_phrase(grammar, '<start>'))
```
<img width="340" alt="Screenshot 2024-10-20 at 18 53 38" src="https://github.com/user-attachments/assets/bab0c812-7ff6-4deb-bbab-63031a8d1fac">


