"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2146/A ---------------------------------------

We call an array balanced if and only if the numbers of occurrences of any of its elements are the same. For example, [1,1,3,3,6,6] and [2,2,2,2] are balanced, 
but [1,2,3,3] is not balanced (the numbers of occurrences of elements 1 and 3 are different). Note that an empty array is always balanced.

You are given a non-decreasing array a consisting of n integers. Find the length of its longest balanced subsequence∗.

∗ A sequence b is a subsequence of a sequence a if b can be obtained from a by the deletion of several (possibly, zero or all) element from arbitrary positions.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of a.

The second line contains n integers a1,a2,…,an (1 ≤ a1 ≤ a2 ≤ ⋯ ≤ an ≤ n) — the elements of a.

Output
For each test case, output a single integer — the length of the longest balanced subsequence of a.

Input:
4
5
1 1 4 4 4
2
1 2
15
1 1 1 1 1 2 2 2 2 3 3 3 4 4 5
5
3 3 3 3 3

Output:
4
2
9
5
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    max_freq = max(freq.values())
    best = 0
    for f in range(1, max_freq + 1):
        count = sum(1 for v in freq.values() if v >= f)
        best = max(best, f * count)
    print(best)