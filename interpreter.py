import sys

class Interpreter:
    def right(self):
        self.current += 1

    def left(self):
        if(self.current == 0):
            self.cells.append(0)
        else:
            self.current -= 1

    def print_cell(self):
        print(chr(self.cells[self.current]))

    def inc(self):
        self.cells[self.current] = (self.cells[self.current] + 1)%256

    def add(self, num):
        self.cells[self.current] = (self.cells[self.current] + num[0])%256

    def sub(self, num):
        self.cells[self.current] = (self.cells[self.current] - num[0])%256

    def dec(self):
        if(self.cells[current] > 0):
            self.cells[self.current] = (self.cells[self.current] - 1)%256

    def do(self, args):
        for operation in args:
            if isinstance(operation, str):
                if operation in self.node_to_func:
                    func = self.node_to_func[operation]
                    func()
                else:
                    func = self.node_to_func_with_args[operation]
                    func()
            elif isinstance(operation, list):
                self.eval(operation)


    def eval(self, commands):
        head, *tail = commands

        if(head in self.node_to_func):
            func = self.node_to_func[head]
            self.func()
        elif(head in self.node_to_func_with_args):
            func = self.node_to_func_with_args[head]
            func(tail)
        elif(isinstance(ast, int)):
            func = self.funcs_with_args.pop()
            self.func(tail)
        else:
            raise ValueError("Maybe you are doing something wrong?")

    def __init__(self, ast):
        self.cells = [0 for x in range(1000)]
        self.current = 0
        self.command_list = ast

        self.node_to_func = {
            'right': self.right,
            'left': self.left,
            'inc': self.inc,
            'dec': self.dec,
            'print': self.print_cell,
        }

        self.node_to_func_with_args = {
            'add': self.add,
            'sub': self.sub,
            'do': self.do,
            'do-before': self.do,
            'do-after': self.do,
        }
