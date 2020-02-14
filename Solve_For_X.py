import re
"""
link: https://www.codewars.com/kata/59c2e2a36bddd2707e000079

kata's name: Solvwe For X

"""


def solve_for_x(equation):
    return equation
    # print(solve_for_x('x - 5 = 20'), 25)
# print(solve_for_x('20 = 5 * x - 5'), 5)


def eq(es, es2=""):
    dat1 = re.findall(r"[0-9x()+-/*=]", es)
    es1 = re.findall(r"\d+|\D", "".join(dat1))
    if es1.index("=") == 1:
        es2 = " ".join(es1[2:]) + " - " + es1[0] + " = 0"
    elif es1.index("=") == len(es1) - 2:
        es2 = " ".join(es1[:len(es1) - 2]) + " - " + es1[-1] + " = 0"
    return es2


def eq1(es):
    df = eq(es).split(" ")
    print(df)
    return df.index("x")


def where(lst):
    if lst.index("x") == 0:
        if lst[lst.index("x") + 1] == "+":
            print("plus")
        elif lst[lst.index("x") + 1] == "-":
            print("minus")
    elif lst.index("x") != 0:
        if lst[lst.index("x") + 1] == "+":
            print(lst[lst.index("x") + 2:])
            return "plus"
        elif lst[lst.index("x") + 1] == "-":
            print(lst[lst.index("x") + 2:])
            return "minus"


def calc(stri1):
    dat1 = re.findall(r"[0-9()+-/*=]", stri1)
    expr = re.findall(r"\d+|\D", "".join(dat1))

    for i in range(len(expr)):
        if expr[i].isdigit():
            expr[i] = float(expr[i])
    while len(expr) > 1:
        if "*" in expr:
            first = expr[expr.index("*") - 1]
            second = expr[expr.index("*") + 1]
            for_paste = first * second
            expr[expr.index("*") - 1: expr.index("*") + 2] = [for_paste]

        elif "/" in expr:
            first = expr[expr.index("/") - 1]
            second = expr[expr.index("/") + 1]
            for_paste = first / second
            expr[expr.index("/") - 1: expr.index("/") + 2] = [for_paste]

        elif "+" in expr:
            first = expr[expr.index("+") - 1]
            second = expr[expr.index("+") + 1]
            for_paste = first + second
            expr[expr.index("+") - 1: expr.index("+") + 2] = [for_paste]

        elif "-" in expr:
            first = expr[expr.index("-") - 1]
            second = expr[expr.index("-") + 1]
            for_paste = first - second
            expr[expr.index("-") - 1: expr.index("-") + 2] = [for_paste]

    return expr[0]

def remove_parenthese(math_expression):
    """
    trasforma l'espressione racchiusa nelle parentesi, in ubn risultato
    ritornando lespressione senza parentesi
    
    """

    dat1 = re.findall(r"[0-9()+-/*=]", math_expression)
    math_expression = re.findall(r"\d+|\D", "".join(dat1))
    print(math_expression)
    start = ""
    stop = ""
    for i in range(len(math_expression)):
        if math_expression[i] == "(":
            start = i
        elif math_expression[i] == ")":
            stop = i
            break
    if start == "":
        return math_expression
    else:
        return "".join(math_expression[:start]) + str(calc(''.join(math_expression[start+1 : stop]))) + ''.join(math_expression[stop + 1:])


print(remove_parenthese("2.23 + (     34.56-34 )* 34 /4 /5"))

# print(calc(input(":  ")))

