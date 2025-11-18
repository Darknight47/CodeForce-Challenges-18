"""

-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2166/A --------------------------------------

You are given a string s of length n, consisting of lowercase letters.

In one operation, you can select an integer i such that 1≤i<n and change si into si+1.

What is the minimum number of operations needed to make every character the same? It can be proved that this is always possible.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 20). The description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 100) — the length of the string.

The following line contains a string s of length n, consisting of lowercase letters.

It is guaranteed that the sum of n over all test cases does not exceed 100.

Output
For each test case, output a single integer — the minimum number of operations needed to make every character the same.

Input:
5
3
qwq
2
aa
4
test
5
abbac
6
abcabc

Output:
1
0
2
4
4
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    lastChar = s[-1]
    ans = 0
    for i in range(sze - 2, -1, -1):
        if(s[i] != lastChar):
            ans += 1
    print(ans)