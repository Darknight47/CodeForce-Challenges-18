"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1882/A ----------------------------------------

You are given a sequence a1,a2,…,an. A sequence b1,b2,…,bn is called good, if it satisfies all of the following conditions:

bi is a positive integer for i=1,2,…,n;
bi ≠ ai for i=1,2,…,n;
b1<b2<…<bn.
Find the minimum value of bn among all good sequences b1,b2,…,bn.
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

Output
For each test case, print a single integer — the minimum value of bn among all good sequences b.

Input:
3
5
1 3 2 6 7
4
2 3 4 5
1
1

Output:
8
4
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    start = 2 if arr[0] == 1 else 1
    ans = [start]
    for i in range(1, sze):
        temp = arr[i]
        b = ans[i - 1]
        if(temp == (b + 1)):
            b += 2
        else:
            b += 1
        ans.append(b)
    print(ans[-1])