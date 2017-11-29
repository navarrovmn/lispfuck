from sys import argv
import pprint
import ox

file_name, lf_source = argv

in_file = open(lf_source)
code = in_file.read()

lexer = ox.make_lexer([
    ('OPENING_BLOCK', r'\('),
    ('CLOSING_BLOCK', r'\)'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('NAME', r'[a-zA-Z_][a-zA-Z_0-9-]*'),
    ('COMMENT', r';(.)*'),
    ('NEW_LINE', r'\n+'),
])

tokens_list = [
    'OPENING_BLOCK',
    'CLOSING_BLOCK',
    'NUMBER',
    'NAME',
]

parser = ox.make_parser([
    ('term : OPENING_BLOCK term CLOSING_BLOCK', lambda opening_block, atom, closing_block: atom),
    ('term : term term', lambda term, term2: (term, term2)),
    ('term : term atom', lambda term, atom: (term, atom)),
    ('term : atom term', lambda atom, term: (atom, term)),
    ('term : atom', lambda term: term),
    ('atom : NUMBER', lambda x: float(x)),
    ('atom : NAME', lambda name: name),
    ('atom : OPENING_BLOCK CLOSING_BLOCK', lambda opening_block, closing_block: ()),
], tokens_list)

pp = pprint.PrettyPrinter(width=60, compact=True)

tokens = lexer(code)
tokens = [value for value in tokens if str(value)[:7] != 'COMMENT' and str(value)[:8] != 'NEW_LINE']
ast = parser(tokens)
pp.pprint(ast)
head, *tail = ast
print(head)
