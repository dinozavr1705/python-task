from time import *
import math
from math import *
n = 123
a = time()
def stirling_alghoritm(n):
    a = sqrt(2 * 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821)
    b = pow(n/math.e,n)
    c =1 + (1 / sqrt(52 * math.e))
    x = a * b + c
    print(x)
    print(f"погрешность = {math.factorial(n) - x}")

stirling_alghoritm(n)
b = time()
c = b - a
s = time()
def factorial(a):
    d = 1
    c = 2
    while c!=a + 1:
        d = d * c
        c = c + 1
    print(d)
    print(f"погрешность = {math.factorial(a) - d}")
factorial(123)
l = time()
k = l - s
if c < k:
    print("метод стерлинга быстрее")
else:
    print("метод перебора быстрее")
