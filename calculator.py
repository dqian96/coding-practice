# A calculator supporting the basic mathematical operations

# TODO: implement precedence

class _ExpressionNode:
    def __init__(self, action, value=''):
        self.action = action
        self.left, self.right = None, None
        self.value = value

    def add_left(self, left_expr):
        self.left = left_expr

    def add_right(self, right_expr):
        self.right = right_expr


def _is_operand(word):
    return word in ('+', '-', '/', '*')


def _get_tokens(expr):
    i = 0  # index

    while i < len(expr):
        c = expr[i]

        if c == ' ':
            # ignore whitespace
            pass
        elif _is_operand(c):
            # operands
            yield c
        elif c in ('(', ')'):
            # brackets
            yield c
        elif c.isdigit():
            # number
            num = []
            while i < len(expr) and expr[i].isdigit():
                num.append(expr[i])
                i += 1
            i -= 1  # compensate for extra increment

            yield ''.join(num)
        else:
            raise Exception('Lexer error; cannot recognize char {}'.format(c))

        i += 1  # next char


def _get_expr_tree(tokens, i=0):
    bracketed = False
    if tokens[i] == '(':
        bracketed = True
        i += 1

    left_node, root = None, None
    while i < len(tokens):
        t = tokens[i]

        if t == ')':
            if bracketed and left_node is not None:
                if root is None:
                    root = left_node
                # finish expr
                i += 1
                break
            else:
                msg = 'Parser error; can\'t close brackets at {}'.format(i)
                raise Exception(msg)

        if left_node is None:
            # expect num
            if t.isnumeric():
                left_node = _ExpressionNode('e', t)
                i += 1
            elif t == '(':
                # recursive expression
                left_node, i = _get_expr_tree(tokens, i)
            else:
                msg = 'Parser error; expects a number at index {}'.format(i)
                raise Exception(msg)
        else:
            # expect operand
            if _is_operand(t):
                root = _ExpressionNode(t)
                root.add_left(left_node)
            elif t.isnumeric():
                msg = 'Parser error; expects an operand at index {}'.format(i)
                raise Exception(msg)

            i += 1
            t = tokens[i]

            # expect expr/number
            if t.isnumeric():
                right_node = _ExpressionNode('e', t)
                i += 1
            if t == '(':
                right_node, i = _get_expr_tree(tokens, i)

            root.add_right(right_node)
            left_node = root

    return (root, i)


def _evaluate(root):
    if _is_operand(root.action):
        lv, rv = _evaluate(root.left), _evaluate(root.right)
        if root.action == '*':
            return lv * rv
        if root.action == '+':
            return lv + rv
        if root.action == '-':
            return lv - rv
        if root.action == '/':
            if rv == 0:
                raise Exception('Semantic error; divide by 0')
            return lv / rv
    elif root.action == 'e':
        # number
        return float(root.value)

    # unknown
    raise Exception('Corrupted parse tree')


def calculate(expr):
    tokens = ['('] + [t for t in _get_tokens(expr)] + [')']
    expr_tree, _ = _get_expr_tree(tokens)
    res = _evaluate(expr_tree)

    return res


def interactive_calculate():
    while True:
        try:
            expr = input('>>> ')
            res = calculate(expr)
            print(res)
        except Exception as e:
            print(str(e))


def test():
    interactive_calculate()


if __name__ == '__main__':
    test()
