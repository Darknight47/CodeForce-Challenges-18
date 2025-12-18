"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/302/A ----------------------------------------------------

Eugeny has array a = a1, a2, ..., an, consisting of n integers. Each integer ai equals to -1, or to 1. Also, he has m queries:

Query number i is given as a pair of integers li, ri (1 ≤ li ≤ ri ≤ n).
The response to the query will be integer 1, if the elements of array a can be rearranged so as the sum ali + ali + 1 + ... + ari = 0, otherwise the response to the query will be integer 0.
Help Eugeny, answer all his queries.

Input
The first line contains integers n and m (1 ≤ n, m ≤ 2·105). The second line contains n integers a1, a2, ..., an (ai = -1, 1). 
Next m lines contain Eugene's queries. The i-th line contains integers li, ri (1 ≤ li ≤ ri ≤ n).

Output
Print m integers — the responses to Eugene's queries in the order they occur in the input.

Input:
2 3
1 -1
1 1
1 2
2 2

Output:
0
1
0
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))
minus = arr.count(-1)
plus = n - minus
for _ in range(m):
    l, r= map(int, input().split())
    #l -= 1
    #subArr = arr[l:r]
    subArrLen = r - l + 1
    if(subArrLen % 2 == 1):
        print("0")
    else:
        required = subArrLen // 2
        if(plus >= required and minus >= required):
            print("1")
        else:
            print("0")