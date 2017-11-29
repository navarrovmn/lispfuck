import sys

cells = [33 for x in range(1000)]
current = 0

print('SASA')

def right():
    global current
    current += 1

def left():
    global current
    if(current == 0):
        cells.append(0)
    else:
        current -= 1

def print_cell():
    print(chr(cells[current]), end='')

def read():
    cells[current] = ord(sys.stdin.read(1))

def loop():
    ...

def inc():
    cells[current] += (cells[current] + 1)%256

def dec():
    if(cells[current] > 0):
        cells[current] += (cells[current] - 1)%256

print('SASA1')

node_to_func = {
    'right': right(),
    'left': left(),
    'inc': inc(),
    'dec': dec(),
    'print': print_cell(),
    'read': read(),
}

print('SASA2')

def eval(ast):
    head, *tail = ast

    if(head in node_to_func):
        node_to_func[head]()
    else:
        raise ValueError('Maybe you are doing something wrong?')


def run_code(ast):
    for x in ast:
        eval(x)

print('SASA3')

test_case = ['inc', 'inc', 'inc', 'print', 'right', 'inc', 'print']

run_code(test_case)
