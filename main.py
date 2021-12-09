import re
import argparse
from typing import Optional, List
from dataclasses import dataclass

from lark import Lark, Transformer, v_args

USAGE = "A command line calculator"


@dataclass
class Token:
    name: str
    value: str


calc_grammar = """
    ?start: sum
          | NAME "=" sum    -> assign_var

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub
        | sum "|" product   -> bitwise_or
        | sum "&" product   -> bitwise_and

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div
        | product "//" atom -> integer_div

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | NAME             -> var
         | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)
    
    def bitwise_or(self, param1, param2) -> float:
        return float(int(param1)|int(param2))

    def bitwise_and(self, param1, param2) -> float:
        return float(int(param1)&int(param2))
        
    def integer_div(self, param1 : int, param2 : int) -> int:
        return int(param1 / param2)



def calculate(formula):
    calc_parser = Lark(calc_grammar, parser='lalr',
                       transformer=CalculateTree())
    result = calc_parser.parse(formula)
    return result


def main():
    parser = argparse.ArgumentParser("calc")
    parser.add_argument("formula", action="store")

    args = parser.parse_args()
    formula = args.formula
    result = calculate(formula)
    if result is not None:
        print(result)


if __name__ == '__main__':
    main()
