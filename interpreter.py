from getch import getche
class Interpreter:
    def right(self):
        self.current += 1

    def left(self):
        if(self.current == 0):
            self.cells.append(0)
        else:
            self.current -= 1

    def print_cell(self):
        print(chr(int(self.cells[self.current])))

    def read_cell(self):
        self.cells[self.current] = ord(getche())
        getche()


    def inc(self):
        self.cells[self.current] = (self.cells[self.current] + 1)%256

    def add(self, num):
        self.cells[self.current] = (self.cells[self.current] + num[0])%256

    def sub(self, num):
        self.cells[self.current] = (self.cells[self.current] - num[0])%256

    def dec(self):
        if(self.cells[self.current] > 0):
            self.cells[self.current] = (self.cells[self.current] - 1)%256

    def do(self, args):
        for operation in args:
            if isinstance(operation, str):
                if operation in self.node_to_func:
                    func = self.node_to_func[operation]
                    func()
                elif operation in self.node_to_func_def:
                    arguments = self.node_to_func_def[operation]
                    self.eval(arguments)
                else:
                    raise ValueError("That operation does not exist")
            elif isinstance(operation, list):
                self.eval(operation)

    def define(self, args):
        head, parenthesis, list_of_commands, *tail = args
        commands = []
        for command in list_of_commands:
            commands.append(command)

        self.node_to_func_def[head] = commands
        self.do(tail)


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

    def loop(self, args):
        while(self.cells[self.current]):
            self.do(args)

    def eval(self, commands):
        head, *tail = commands

        if(head in self.node_to_func):
            func = self.node_to_func[head]
            func()
        elif(head in self.node_to_func_with_args):
            func = self.node_to_func_with_args[head]
            func(tail)
        else:
            raise ValueError("That operation does not exist")

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
            'read': self.read_cell,
        }

        self.node_to_func_with_args = {
            'add': self.add,
            'sub': self.sub,
            'do': self.do,
            'do-before': self.do_before,
            'do-after': self.do_after,
            'loop': self.loop,
            'def': self.define,
        }

        self.node_to_func_def = {}
