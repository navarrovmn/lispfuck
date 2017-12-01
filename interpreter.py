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

    def read_cell(self):
        self.cells[self.current] = int(sys.stdin.read(1))

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

    def do_after(self, args):
        head, *tail = args
        another_tail = []
        for x in tail:
            if isinstance(x, list):
                for k in x:
                    another_tail.append(['do', k, head])
            else:
                another_tail.append(x)
        another_tail.insert(0, 'do')
        self.eval(another_tail)

    def do_before(self, args):
        head, *tail = args
        another_tail = []
        for x in tail:
            if isinstance(x, list):
                for k in x:
                    another_tail.append(['do', head, k])
            else:
                another_tail.append(x)
        another_tail.insert(0, 'do')
        self.eval(another_tail)

    def eval(self, commands):
        head, *tail = commands

        if(head in self.node_to_func):
            func = self.node_to_func[head]
            func()
        elif(head in self.node_to_func_with_args):
            func = self.node_to_func_with_args[head]
            func(tail)
        elif(isinstance(head, int)):
            func = self.funcs_with_args.pop()
            func(tail)
        else:
            raise ValueError("Maybe you are doing something wrong?")

    def __init__(self, ast):
        self.cells = [97 for x in range(1000)]
        self.current = 0
        self.command_list = ast

        self.node_to_func = {
            'right': self.right,
            'left': self.left,
            'inc': self.inc,
            'dec': self.dec,
            'print': self.print_cell,
            'read': self.read_cell,
        }

        self.node_to_func_with_args = {
            'add': self.add,
            'sub': self.sub,
            'do': self.do,
            'do-before': self.do_before,
            'do-after': self.do_after,
        }

test = ["do-after", "print", ["inc", "inc"]]
test2 = ["do", ["add", 2], "print"]
test3 = ["do-before", "print", ["inc", "inc"]]
test4 = ["do", "read", ["add", 97], "print"]

interp = Interpreter(test4)
interp.eval(interp.command_list)
