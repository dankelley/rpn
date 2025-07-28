#!/usr/bin/env python3
debug = False
version = "0.0.3"
def rpn_help():
  return("""Examples:
  rpn e                          # Euler's number
  rpn e -d 10                    # Euler's number, with more digits
  rpn pi                         # Pi
  rpn 10 35                      # Place 2 items on stack
  rpn 10 2 /                     # Equals 5; also try 'x', '+' and '-'
  rpn 45 sin                     # sin, cos and tan take angle in degrees
  rpn 1 asin                     # asin, acos and atan return an angle in degrees
  rpn 10 35 exch                 # [35.0, 10.0] (... exchange those items)
  rpn 10 35 pop                  # 35.0 (... remove last-added item)
  rpn 10 ln                      # natural log
  rpn 10 log                     # base-10 log
  rpn 10 2 ^                     # exponentiation
  rpn 2143 22 / 0.25 ^           # Ramanujan formula for Pi to 9 digits
  rpn 2143 22 / 0.25 ^ pi approx # Check Ramanujan, approximately
  rpn 2143 22 / 0.25 ^ pi equal  # Check Ramanujan, equally

Saving 'def' quantities to a file
  rpn -l conversions.json '32 - 5 x 9 /' _f2c def
  rpn -l conversions.json '9 x 5 / 32 +' _c2f def
  rpn -l conversions.json 20 _c2f _f2c

Built-in values
  e, pi

Unary operators (replace last item on stack):
  cos, sin, tan (in degrees),
  acos, asin, atan, (in degrees)
  deg, rad, # convert to degrees or to radians
  cosh, sinh, tanh (not in degrees)
  acosh, asinh, atanh, (not in degrees)
  exp, ln, log, sqr, sqrt
  chs, exp, inv
Binary operators:
  +, -, /, x, ^,
  approx, APPROX, equal, EQUAL
Stack operators:
  dup, exch, pop
Definitional operators:
  def

Puzzles: without running rpn, guess the meaning of the following
  rpn pi 4 / deg sin
  rpn 45 sin sqr 45 cos sqr +
  rpn 1e-7 _eps def 1 _eps + sqr 1 sqr - _eps /

Installation:
  Visit http://www.github.com/dankelley/rpn and download `rpn.py`. Then make
  it executable (with `chmod +x rpn.py` on unix machines), and put it,
  or an alias, in your unix "path" (I alias it to `~/bin/,rpn` because
  I like using a comma at the start of non-standard local commands.)
    """)

def rpn(tokens, show_stack = False, library=None, digits=8, help = False):
    import sys
    import math

    debug = False
    stack = []
    dict_def = {}
    if library and os.path.exists(library):
        with open(library) as file:
            dict_def = json.load(file)
        if debug:
            print(f"in rpn(), based on {library}, defined dict_def = {dict_def}")

    def approx(a, b, tolerance=1.490116e-08):
        diff = abs(a - b)
        return 1.0 if diff < tolerance else float(diff * b < tolerance)

    def checkstack(n, token):
        nstack = len(stack)
        if nstack < n:
            print(f'The stack only has {nstack} items, but {token} requires at least {n} items; next is stack:')
            print(stack)
            sys.exit(1)

    i = 0
    while i < len(tokens):
        token = tokens[i]
        slen = len(stack)
        nexttoken = tokens[i+1] if i < len(tokens) - 1 else None

        if debug:
            print(f'token: {token}, next: {nexttoken}')

        def binary_op(fn):
            checkstack(2, token)
            stack[slen - 2] = fn(float(stack[slen-2]), float(stack[slen-1]))
            stack.pop()

        def unary_op(fn):
            stack[slen - 1] = fn(float(stack[slen-1]))

        if token == "+": binary_op(lambda a, b: a + b)
        elif token == "-": binary_op(lambda a, b: a - b)
        elif token == "x": binary_op(lambda a, b: a * b)
        elif token == "/": binary_op(lambda a, b: a / b)
        elif token == "^": binary_op(lambda a, b: math.pow(a, b))
        elif token == "EQUAL":
            checkstack(2, token)
            if stack[-1] != stack[-2]:
                print(f"EQUAL test failed on {stack[-2]} and {stack[-1]}")
                sys.exit(2)
            stack.pop(); stack.pop()
        elif token == "equal": binary_op(lambda a, b: float(a == b))
        elif token == "approx": binary_op(lambda a, b: float(approx(a, b)))
        elif token == "APPROX":
            checkstack(2, token)
            if approx(float(stack[-2]), float(stack[-1])) != 1.0:
                print(f"APPROX test failed on {stack[-2]} and {stack[-1]}")
                sys.exit(2)
            stack.pop(); stack.pop()
        elif token == "exch":
            checkstack(2, token)
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif token == "pop":
            stack.pop()
        elif token == "dup":
            stack.append(stack[-1])
        elif token == "def":
            checkstack(2, token)
            name = stack.pop()
            value = stack.pop()
            if not isinstance(name, str) or not name.startswith("_"):
                print(f'cannot define "{name}" because it does not start with "_"')
                sys.exit(1)
            if name in dict_def and options.library:
                print(f'Redefining "{name}" in library "{options.library}"')
            dict_def[name] = value
            if options.show_stack:
                print(dict_def)
        elif token == "chs": unary_op(lambda a: -a)
        elif token == "sqrt": unary_op(math.sqrt)
        elif token == "sqr": unary_op(lambda a: a ** 2)
        elif token == "inv": unary_op(lambda a: 1.0 / a)
        elif token == "sin": unary_op(lambda a: math.sin(math.radians(a)))
        elif token == "sinh": unary_op(math.sinh)
        elif token == "asin": unary_op(lambda a: math.degrees(math.asin(a)))
        elif token == "asinh": unary_op(math.asinh)
        elif token == "cos": unary_op(lambda a: math.cos(math.radians(a)))
        elif token == "cosh": unary_op(math.cosh)
        elif token == "acos": unary_op(lambda a: math.degrees(math.acos(a)))
        elif token == "acosh": unary_op(math.acosh)
        elif token == "tan": unary_op(lambda a: math.tan(math.radians(a)))
        elif token == "tanh": unary_op(math.tanh)
        elif token == "atan": unary_op(lambda a: math.degrees(math.atan(a)))
        elif token == "atanh": unary_op(math.atanh)
        elif token == "deg": unary_op(math.degrees)
        elif token == "rad": unary_op(math.radians)
        elif token == "exp": unary_op(math.exp)
        elif token == "ln": unary_op(math.log)
        elif token == "log": unary_op(math.log10)
        elif token == "pi": stack.append(math.pi)
        elif token == "e": stack.append(math.e)
        elif token in dict_def:
            val = dict_def[token]
            if nexttoken == "def":
                stack.append(token)
            elif isinstance(val, str) and " " in val:
                tokens = tokens[:i] + val.split() + tokens[i+1:]
                i -= 1
            else:
                stack.append(val)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                stack.append(token)
        if show_stack:
            print("%6s" % token, stack)
        i += 1

    if debug:
        print(f"dict_def={dict_def}")
    if library and dict_def:
        with open(library, "w") as file:
            json.dump(dict_def, file, indent=4)

    fmt = f'%.{digits}f'
    if len(stack) == 1:
        print(fmt % float(stack[0]))
    elif len(stack) > 1:
        print(stack)
    if show_stack and dict_def:
        print(dict_def)


if __name__ == "__main__":
    import argparse
    import os
    import json
    import sys
    parser = argparse.ArgumentParser(prog='rpn',
                                     description='An RPN commandline calculator',
                                     usage='rpn [-v] [-h] [-s] [-d DIGITS] [-l FILENAME] [tokens]',
                                     epilog=rpn_help(),
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--digits', type=int, default=6, help='number of digits to show in final (singleton) result')
    #parser.add_argument('-h', '--help', action='store_true', help='DAN DAN DAN')
    parser.add_argument('-l', '--library', type=str, help='name of a file to save/retrieve def items')
    parser.add_argument('-s', "--show_stack", action='store_true', help='show stack during processing')
    parser.add_argument('-v', "--version", action='store_true', help='show version number and then quit')
    parser.add_argument("tokens", nargs="*")
    options, args = parser.parse_known_args()

    if options.version:
        print(f'Version {version}')
        sys.exit(0)

    if debug:
        print(options)

    rpn(options.tokens, show_stack = options.show_stack, library = options.library, digits=options.digits)

