"""

------------------------------------------ Link for the challenge: https://codeforces.com/contest/2176/problem/B ------------------------------------------------

You are given a binary string s1s2…sn, containing at least one 1. You want to obtain a binary string of the same length, consisting only of 1s. 
To do this, you can perform the following operation any number of times:

Choose a number d (1 ≤ d ≤ n) and consider the string t as a cyclic right shift of the string s by d, or, more formally, t=sn−d+1…sns1…sn−d. 
After that, for all j for which tj=1, perform sj:=1. 
The described operation costs d coins, where d is the chosen shift amount.

Note that the positions j in the string s, where initially sj=1, remain equal to 1 even if tj=0.

You need to determine the minimum number of coins that can be spent so that the string s consists only of 1s after all operations.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains the number n (1 ≤ n ≤ 2⋅10^5) — the size of the given binary string.

The second line of each test case contains a binary string of length n, each element of which is either 0 or 1.

It is guaranteed that at least one character in each string is equal to 1.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, output the answer to it — the minimum possible number of coins that you can spend to make all characters in the string equal to 1.

Input:
5
1
1
3
101
4
0110
11
10101010100
2
11

Output:
0
1
2
2
0
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    # doubling the string to handle circular runs
    doubled = s + s

    max_zero_run = 0
    current_run = 0

    for ch in doubled:
        if ch == '0':
            current_run += 1
            max_zero_run = max(max_zero_run, current_run)
        else:
            current_run = 0
    print(min(max_zero_run, sze))