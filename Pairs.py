"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1656/A ------------------------------------------------

You are given an array a1,a2,…,an of positive integers. A good pair is a pair of indices (i,j) with 1 ≤ i, j ≤ n such that, for all 1≤k≤n, the following equality holds:

|ai−ak|+|ak−aj|=|ai−aj|,

where |x| denotes the absolute value of x.

Find a good pair. Note that i can be equal to j.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 10^5) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) where ai is the i-th element of the array.

The sum of n for all test cases is at most 2⋅10^5.

Output
For each test case, print a single line with two space-separated indices i and j which form a good pair of the array. 
The case i=j is allowed. It can be shown that such a pair always exists. If there are multiple good pairs, print any of them.

Input:
3
3
5 2 7
5
1 4 2 2 3
1
2

Output:
2 3
1 2
1 1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    min_val = max_val = arr[0]
    min_idx = max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val, min_idx = arr[i], i
        elif arr[i] > max_val:
            max_val, max_idx = arr[i], i
    print(max_idx + 1, min_idx + 1)