"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1750/B --------------------------------

A binary string is a string consisting only of the characters 0 and 1. You are given a binary string s.

For some non-empty substring† t of string s containing x characters 0 and y characters 1, define its cost as:

x⋅y, if x>0 and y>0;
x2, if x>0 and y=0; y2, 
if x=0 and y>0.
Given a binary string s of length n, find the maximum cost across all its non-empty substrings.

† A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^5) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the string s.

The second line of each test case contains a binary string s of length n.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print a single integer — the maximum cost across all substrings.

Input:
6
5
11100
7
1100110
6
011110
7
1001010
4
1000
1
0

Output:
9
12
16
12
9
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    max_run = 1
    current_run = 1
    zeros = 0
    ones = 0
    if s[0] == '0':
        zeros += 1
    else:
        ones += 1

    # Traverse the string
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 1

        # Count zeros and ones
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1

    temp1 = max_run**2
    temp2 = zeros * ones
    print(max(temp1, temp2))