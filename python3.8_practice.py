#  Walrus operator
from typing import Final

walrus = True
print(walrus)  # typical way of creating variable and assign variable

print(walrus := True)

inputs = []
# while True:
#     text = input("Writing input... ")
#     if text.lower() in 'quit':
#         break
#     inputs.append(text)
#
# print(inputs)

# while (text := input("Write greetings...")).lower() != 'quit':
#     inputs.append(text)
#
# print(inputs)

def inc(x):
    print(x + 1)

inc(x=210)
inc(110)

def inc(x, /, a, b):
    print(x + 1)

# inc(x=332)  # gives error
inc(332, 10, b = 20)

def f(x, /, a, b, c=1000, *, n, m=100):
    print(x, a, b, c, n, m, sep=',')

f(111, 10, b=20, n=30)

def headline(text, /, border="♦", *, width=50):
    print(f' {text} '.center(width, border))

headline("Positional-only Arguments")

a = pow(10, 2)
print(a)
# print(help(pow))

def f(a, / , **kwargs):
    print(a, *kwargs, kwargs, sep=',')

params = {'a' :1000, 'b': 2000}
f(1111, **params)

import math
r = 3.6

print(f"A circle with radius {r} has area {math.pi * r * r:.2f}")
python = 3.8
print(f"{python}")
print(f"{python=}")

from itertools import accumulate
print(list(accumulate([10, 5, 30, 15], initial=1000)))

pi: Final[float] = 3.1415926536
var: Final = 111
# var: Final[int] = 111
print(var)


def f(a: int) -> int:
    return a * 10

print(f(20))
print(f('a'))






