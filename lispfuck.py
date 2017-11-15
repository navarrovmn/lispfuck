import ox

op_to_desc = {
    'read': 'input function',
    'left': 'walk left',
    'right': 'walk right',
    'inc': 'increment tape',
    'add': 'increment tape',
    'dec': 'decrement tape',
    'print': 'print value'
}

treat_list = lambda term, other_term: (term, other_term)
treat_atom = lambda op: (op_to_desc[op], op)

lexer = ox.make_lexer([
    ('OPENING_BLOCK', r'\('),
    ('CLOSING_BLOCK', r'\)'),
    ('RIGHT_TAPE', r'right'),
    ('LEFT_TAPE', r'left'),
    ('SUM', r'inc|add'),
    ('SUB', r'dec'),
    ('PRINT', r'print'),
    ('READ', r'read'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('NAME', r'[a-zA-Z_][a-zA-Z_0-9]*'),
])

tokens_list = [
    'NUMBER',
    'OPENING_BLOCK',
    'CLOSING_BLOCK',
    'RIGHT_TAPE',
    'LEFT_TAPE',
    'SUM',
    'SUB',
    'PRINT',
    'READ'
]

parser = ox.make_parser([
    ('lisp_list: lisp_list atom', treat_list),
    ('lisp_list: atom', treat_atom),
    ('atom: RIGHT_TAPE', treat_atom),
    ('atom: LEFT_TAPE', treat_atom),
    ('atom: SUM', treat_atom),
    ('atom: SUB', treat_atom),
    ('atom: PRINT', treat_atom),
    ('atom: READ', treat_atom),
    ('atom: NUMBER', lambda number : ('simple_number', float(number))),
    ('atom: NAME', lambda name : ('simple_name', name)),
], tokens_list)

