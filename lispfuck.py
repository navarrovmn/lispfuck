from sys import argv
import ox

file_name, lf_source = argv

in_file = open(lf_source)
text = in_file.readlines()

def is_comment(line):
    count = 0
    while line[count] == ' ':
        count+=1
    if line[count] == ';':
         return True
    return False

code = ""

for line in text:
    if is_comment(line):
         continue
    code += line.strip('\n')

print(code)

lexer = ox.make_lexer([
    ('OPENING_BLOCK', r'\('),
    ('CLOSING_BLOCK', r'\)'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('NAME', r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('COMMENT', r';')
])

tokens_list = [
    'OPENING_BLOCK',
    'CLOSING_BLOCK',
    'NUMBER',
    'NAME',
        'COMMENT',
]

parser = ox.make_parser([
    ('term : OPENING_BLOCK term CLOSING_BLOCK', lambda opening_block, atom, closing_block: (opening_block, atom, closing_block)),
    ('term : term term', lambda term, term2: (term, term2)),
    ('term : term atom', lambda term, atom: (term, atom)),
    ('term : atom term', lambda atom, term: (atom, term)),
    ('term : atom', lambda term: term),
    ('atom : NUMBER', lambda x: float(x)),
    ('atom : NAME', lambda name: name),
], tokens_list)

tokens = lexer(code)
ast = parser(tokens)
print('tokens: ', tokens)
print('ast: ', ast)
