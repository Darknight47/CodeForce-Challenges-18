"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2170/A ---------------------------------

Consider an n×n grid filled with numbers as follows:

the first row contains integers from 1 to n from left to right;
the second row contains integers from (n+1) to 2n from left to right;
this pattern continues until the n-th row, which contains integers from (n2−n+1) to n2 from left to right.
Let's define the cost of a cell as its value plus the sum of its neighboring cells' values. Two cells are considered neighboring if they share a side.

Your task is to calculate the maximum cost among all cells in the grid.

The grid for n=4 and the optimal answer for it. The yellow cell has the maximum possible cost; the green cells are its neighbors. The cost of the cell is 15+11+14+16=56.
Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The only line of each test case contains a single integer n (1 ≤ n ≤ 100).

Output
For each test case, print a single integer — the maximum cost among all cells in the grid.

Input:
5
1
2
3
4
5

Output:
1
9
29
56
95
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1):
        print(1)
    elif(n == 2):
        print(9)
    else:
        first = n * n
        second = first - 1
        third = first - 2
        fourth = second - n
        temp1 = first + second + third + fourth
        first = (n * n) - n
        second = first - 1
        third = second - 1
        fourth = second - n
        fifth = second + n
        temp2 = first + second + third + fourth + fifth
        print(max(temp1, temp2))