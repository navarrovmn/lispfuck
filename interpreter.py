import sys

cells = [0 for x in range(1000)]
current = 0

def right():
    global current
    current += 1

def left():
    global cells
    global current

    if(current == 0):
        cells.append(0)
    else:
        current -= 1

def print_cell():
    global cells
    global current

    print(cells[current])
    # print(chr(cells[current]), end='')

def read():
    ...

def loop():
    ...

def inc():
    global cells
    global current

    cells[current] = (cells[current] + 1)%256
    print(cells[current])

def dec():
    global cells
    global current

    if(cells[current] > 0):
        cells[current] = (cells[current] - 1)%256

node_to_func = {
    'right': right(),
    'left': left(),
    'inc': inc(),
    'dec': dec(),
    'print': print_cell(),
    'read': read(),
}

def eval(ast):
    if(ast in node_to_func):
        print(ast)
        node_to_func[ast]
    else:
        raise ValueError('Maybe you are doing something wrong?')


def run_code(ast):
    for x in ast:
        eval(x)

test_case = ['inc', 'inc', 'inc', 'print', 'right', 'inc', 'print']

run_code(test_case)
