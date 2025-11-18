"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1937/A -----------------------------

You are given an array a1,a2,…,an. Initially, ai=i for each 1 ≤ i ≤ n.

The operation swap(k) for an integer k≥2 is defined as follows:

Let d be the largest divisor† of k which is not equal to k itself. Then swap the elements ad and ak.
Suppose you perform swap(i) for each i=2,3,…,n in this exact order. Find the position of 1 in the resulting array. In other words, find such j that aj=1 after performing these operations.

† An integer x is a divisor of y if there exists an integer z such that y=x⋅z.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains one integer n (1 ≤ n ≤ 10^9) — the length of the array a.

Output
For each test case, output the position of 1 in the resulting array.

Input:
4
1
4
5
120240229

Output:
1
4
4
67108864
"""
import math
cases = int(input())
for _ in range(cases):
    num = int(input())
    ans = 2 ** int(math.log2(num))
    print(ans)