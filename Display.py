"""

-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/747/A -----------------------------------

A big company decided to launch a new series of rectangular displays, and decided that the display must have exactly n pixels.

Your task is to determine the size of the rectangular display — the number of lines (rows) of pixels a and the number of columns of pixels b, so that:

there are exactly n pixels on the display;
the number of rows does not exceed the number of columns, it means a ≤ b;
the difference b - a is as small as possible.

Input
The first line contains the positive integer n (1 ≤ n ≤ 106) — the number of pixels display should have.

Output
Print two integers — the number of rows and columns on the display.


Input:
8

Output:
2 4
"""
import math
n = int(input())
a = math.floor(math.sqrt(n))
b = 0
while a > 0:
    if(n % a == 0):
        b = n // a
        break
    a -= 1
print(a, b)