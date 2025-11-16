"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2153/A --------------------------------------------

There are n apple trees arranged in a circle. Each tree bears exactly one apple, and the beauty of the apple on the i-th tree is given by bi for all 1 ≤ i ≤ n. You start in front of tree 1.

At each tree, you may choose to either eat the apple or skip it. After making your choice, you move to the next tree: from tree i, 
you move to tree i+1 for 1 ≤ i ≤ n−1, and from tree n, you move back to tree 1. This process continues indefinitely as you move through the trees in a cycle.

However, you have a special condition: you may only eat an apple if its beauty is strictly greater than the beauty of the last apple you ate. For example, if b=[2,1,2,3]
and you eat the apple on tree 1 (beauty 2), you cannot eat the apples on trees 2 and 3 because their beauties are not greater than 2. 
However, you may eat the apple on tree 4 since b4 = 3 > 2.

Note that you are allowed to skip an apple when you first encounter it, and you can choose to eat it later on a subsequent cycle.

Your task is to determine the maximum number of apples you can eat if you make optimal decisions on when to eat or skip each apple.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of apple trees.

The second line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ n) — the beauty of the apples on the trees.

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, output a single integer representing the maximum number of apples you can eat.

Input:
3
4
2 2 2 2
5
1 4 5 1 2
6
5 4 2 1 2 3

Output:
1
4
5
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    print(len(tempSet))