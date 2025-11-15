"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1884/A --------------------------------------

A positive integer is called k-beautiful, if the digit sum of the decimal representation of this number is divisible by k†. 
For example, 9272 is 5-beautiful, since the digit sum of 9272 is 9+2+7+2=20.

You are given two integers x and k. Please find the smallest integer y≥x which is k-beautiful.

† An integer n is divisible by k if there exists an integer m such that n=k⋅m.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains two integers x and k (1 ≤ x ≤ 10^9, 1 ≤ k ≤ 10).

Output
For each test case, output the smallest integer y≥x which is k-beautiful.

Input:
6
1 5
10 8
37 9
777 3
1235 10
1 10

Output:
5
17
45
777
1243
19
"""
cases = int(input())
for _ in range(cases):
    x, k = map(int, input().split())
    xcopy = x
    addition = 0
    while True:
        xcopy = x + addition
        total = 0
        while xcopy > 0:
            total += xcopy % 10
            xcopy //= 10
        if(total % k == 0):
            print(x + addition)
            break
        addition += 1    