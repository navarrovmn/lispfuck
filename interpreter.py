import sys

funcs_with_args = []
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
    print(chr(cells[current]))

def inc():
    global current

    cells[current] = (cells[current] + 1)%256

def add(num):
    global current

    cells[current] = (cells[current] + num[0])%256

def sub(num):
    global current

    cells[current] = (cells[current] - num[0])%256

def dec():
    global current

    if(cells[current] > 0):
        cells[current] = (cells[current] - 1)%256

# todo

def do(args):
    for operation in args:
        print(operation)
        if isinstance(operation, str):
            if operation in node_to_func:
                func = node_to_func[operation]
                func()
            else:
                func = node_to_func_with_args[operation]
                func(tail)
        elif isinstance(operation, list):
            eval(operation)


node_to_func = {
    'right': right,
    'left': left,
    'inc': inc,
    'dec': dec,
    'print': print_cell,
}

node_to_func_with_args = {
    'add': add,
    'sub': sub,
    'do': do,
    'do-before': do,
    'do-after': do,
}

def eval(ast):
    head, *tail = ast

    if(head in node_to_func):
        func = node_to_func[head]
        func()
    elif(head in node_to_func_with_args):
        func = node_to_func_with_args[head]
        func(tail)
    elif(isinstance(ast, int)):
        func = funcs_with_args.pop()
        func(tail)
    else:
        raise ValueError("Maybe you are doing something wrong?")


program = ['do', 'inc', 'print', ['do', 'print', ['add', 2], 'print']]
eval(program)
