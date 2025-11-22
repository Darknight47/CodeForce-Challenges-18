"""
----------------------------------------- Link for the challenge: https://codeforces.com/contest/1867/problem/A -------------------------------------

green_gold_dog has an array a of length n, and he wants to find a permutation b of length n such that the number of distinct numbers in the element-wise difference between array a and permutation b is maximized.

A permutation of length n is an array consisting of n distinct integers from 1 to n in any order. For example, [2,3,1,5,4] is a permutation, 
but [1,2,2] is not a permutation (as 2 appears twice in the array) and [1,3,4] is also not a permutation (as n=3, but 4 appears in the array).

The element-wise difference between two arrays a and b of length n is an array c of length n, where ci = ai−bi (1≤i≤n).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 4⋅10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 4⋅10^4).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 4⋅10^4.

Output
For each test case, output n numbers - a suitable permutation b. If there are multiple solutions, print any of them.

Input:
3
1
100000
2
1 1
3
10 3 3

Output:
1 
2 1 
1 3 2 
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    #perm = list(range(1, n+1))

    # Sort arr ascending, keep original indices
    arr_sorted = sorted([(val, idx) for idx, val in enumerate(arr)])
    
    # Assign permutation values descending
    perm_values = list(range(n, 0, -1))  # [n, n-1, ..., 1]
    
    b = [0] * n
    for (val, idx), p in zip(arr_sorted, perm_values):
        b[idx] = p
    
    print(*b)