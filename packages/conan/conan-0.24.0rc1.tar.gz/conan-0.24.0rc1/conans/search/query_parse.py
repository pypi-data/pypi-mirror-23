from conans.util.log import logger


def is_operator(el):
    return el in ["|", "&"]


def _parse_expression(subexp):
    '''Expressions like:
     compiler.version=12
     compiler="Visual Studio"
     arch="x86"
     Could be replaced with another one to parse different queries'''
    ret = ""
    quoted = False
    for char in subexp:
        if char in ['"', "'"]:  # Fixme: Mix quotes
            quoted = not quoted
            ret += char
            continue

        if quoted:
            ret += char
        elif char == " " or is_operator(char) or char in [")", "("]:
            break
        else:
            ret += char

    if "=" not in ret:
        raise Exception("Invalid expression: %s" % ret)

    return ret


def evaluate_postfix(postfix, evaluator):
    """
    Evaluates a postfix expression and returns a boolean
    @param postfix:  Postfix expression as a list
    @param evaluator: Function that will return a bool receiving expressions
                      like "compiler.version=12"
    @return: bool
    """
    if not postfix:  # If no query return all?
        return True

    stack = []
    for el in postfix:
        if not is_operator(el):
            stack.append(el)
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            if not isinstance(o1, bool):
                o1 = evaluator(o1)
            if not isinstance(o2, bool):
                o2 = evaluator(o2)

            if el == "|":
                res = o1 or o2
            elif el == "&":
                res = o1 and o2
            stack.append(res)
    if len(stack) != 1:
        raise Exception("Bad stack: %s" % str(stack))
    elif not isinstance(stack[0], bool):
        return evaluator(stack[0])  # Single Expression without AND or OR
    else:
        return stack[0]


def infix_to_postfix(exp):
    """
    Translates an infix expression to postfix using an standard algorithm
    with little hacks for parse complex expressions like "compiler.version=4"
    instead of just numbers and without taking in account the operands priority
    except the priority specified by the "("

    @param exp: String with an expression with & and | operators,
        e.j: "os=Windows & (compiler=gcc | compiler.version=3)"
        e.j: "os=Windows AND (compiler=gcc or compiler.version=3)"
    @return List with the postfix expression
    """

    # To ease the parser, operators only with one character
    exp = exp.replace(" AND ", "&").replace(" OR ", "|").replace(" and ", "&").replace(" or ", "|")
    output = []
    stack = []

    i = -1
    while(i < len(exp) - 1):
        i += 1
        char = exp[i]
        if char == " ":  # Ignore spaces between expressions and operators
            continue
        if char == ")":  # Pop the stack until "(" and send them to output
            popped = None
            while(popped != "(" and stack):
                popped = stack.pop()
                if popped != "(":
                    output.append(popped)
            if popped != "(":
                raise Exception("Bad expression, not balanced parenthesis")
        elif is_operator(char):
            # Same operations has the same priority
            # replace this lines if the operators need to have
            # some priority
            if stack and is_operator(stack[:-1]):
                popped = stack.pop()
                output.append(popped)
            stack.append(char)
        elif char == "(":
            stack.append("(")
        else:  # Parse an expression, in our case something like "compiler=gcc"
            logger.debug("Parsing expression from : %s" % exp[i:])
            expr = _parse_expression(exp[i:])
            logger.debug("Parsed expression: %s" % expr)
            i += len(expr) - 1
            output.append(expr)

    # Append remaining elements
    if "(" in stack:
        raise Exception("Bad expression, not balanced parenthesis")
    output.extend(stack)
    return output
