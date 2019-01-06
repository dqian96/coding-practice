from collections import namedtuple

Instruction = namedtuple('Instruction', 'cmd args')

class StackMachine():

    def __init__(self):
        self.stack = []

    def _check_num_args(self, actual, expected):
        if actual != expected:
            msg = 'expected {} got {} num args'.format(expected, actual)
            raise Exception(msg)

    def _push(self, *args):
        self._check_num_args(len(args), 1)
        self.stack.append(args[0])

    def _add(self, *args):
       self._check_num_args(len(args), 0)
       if len(self.stack) < 2:
           raise Exception('cannot add less than 2 args')

       a, b = self.stack.pop(), self.stack.pop()
       c = int(a) + int(b)
       self.stack.append(str(c))

    def _subtract(self, *args):
       self._check_num_args(len(args), 0)
       if len(self.stack) < 2:
           raise Exception('cannot sub less than 2 args')

       a, b = self.stack.pop(), self.stack.pop()
       c = int(a) - int(b)
       self.stack.append(str(c))


    def _print(self, *args):
       self._check_num_args(len(args), 0)
       if len(self.stack) < 1:
           raise Exception('cannot print no values')
       print(self.stack[-1])


    def _return(self, *args):
       self._check_num_args(len(args), 0)
       if len(self.stack) < 1:
           raise Exception('cannot return no values')
       return self.stack[-1]

    _INSTRUCTIONS_SET = {
        'push': _push,
        'add': _add,
        'subtract': _subtract,
        'print': _print,
        'return': _return,
    }

    def _parse(self, program):
        def text_to_instruction(instr):
            tokens = instr.split()
            cmd = tokens[0]
            if cmd not in StackMachine._INSTRUCTIONS_SET.keys():
                raise Exception("unknown command")

            return Instruction(cmd, tokens[1:])

        lines = program.split('\n')
        filtered_lines = [l for l in lines if not l.isspace()]
        instructions = [text_to_instruction(instr) for instr in filtered_lines]
        return instructions

    def run(self, program):
        instructions = self._parse(program)

        for instr in instructions:
            operation = StackMachine._INSTRUCTIONS_SET[instr.cmd]
            code = operation(self, *instr.args)

            if instr.cmd == 'return':
                # quit program
                return code


def test():
    program = """\
        push 5
        push 3
        push 1
        add
        subtract
        print
        return
    """

    machine = StackMachine()

    res = machine.run(program)
    print('exit code: {}'.format(res))


def main():
    test()


if __name__ == '__main__':
    main()
