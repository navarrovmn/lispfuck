import ox

lexer = ox.make_lexer([
    ('OPENING_BLOCK', r'\('),
    ('CLOSING_BLOCK', r'\)'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('NAME', r'[a-zA-Z_][a-zA-Z_0-9]*'),
])

tokens_list = [
    'OPENING_BLOCK',
    'CLOSING_BLOCK',
    'NUMBER',
    'NAME',
]

parser = ox.make_parser([
    ('term : OPENING_BLOCK term CLOSING_BLOCK', lambda opening_block, atom, closing_block: (opening_block, atom, closing_block)),
    ('term : term atom', lambda term, atom: (term, atom)),
    ('term : atom term', lambda atom, term: (atom, term)),
    ('term : atom', lambda term: term),
    ('atom : NUMBER', lambda x: float(x)),
    ('atom : NAME', lambda name: name),
], tokens_list)

expr = input('expr: ')
tokens = lexer(expr)
ast = parser(tokens)
print('tokens: ', tokens)
print('ast: ', ast)
