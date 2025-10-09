"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2035/A -----------------------------------

There are n rows of m people. Let the position in the r-th row and the c-th column be denoted by (r,c). 
Number each person starting from 1 in row-major order, i.e., the person numbered (r−1)⋅m+c is initially at (r,c).

The person at (r,c) decides to leave. To fill the gap, let the person who left be numbered i. 
Each person numbered j>i will move to the position where the person numbered j−1 is initially at. The following diagram illustrates the case where n=2, m=3, r=1, and c=2.

Calculate the sum of the Manhattan distances of each person's movement. If a person was initially at (r0,c0) and then moved to (r1,c1), the Manhattan distance is |r0−r1|+|c0−c1|.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each testcase contains 4 integers n, m, r, and c (1 ≤ r ≤ n ≤ 10^6, 1 ≤ c ≤ m ≤ 10^6), where n is the number of rows, 
m is the number of columns, and (r,c) is the position where the person who left is initially at.

Output
For each test case, output a single integer denoting the sum of the Manhattan distances.

Input:
4
2 3 1 2
2 2 2 1
1 1 1 1
1000000 1000000 1 1

Output:
6
1
0
1999998000000
"""
cases = int(input())
for _ in range(cases):
    n, m, r, c = map(int, input().split())
    col = m - c
    row = n - r
    ans = col + row * (2 * m - 1)
    print(ans)