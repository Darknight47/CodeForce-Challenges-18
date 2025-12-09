"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1733/A ----------------------------------------

You are given an array a with n integers. You can perform the following operation at most k times:

Choose two indices i and j, in which i mod k = j mod k (1 ≤ i < j ≤ n).
Swap ai and aj.
After performing all operations, you have to select k consecutive elements, and the sum of the k elements becomes your score. Find the maximum score you can get.

Here xmody denotes the remainder from dividing x by y.

Input
The first line contains one integer t (1 ≤ t ≤ 600) — the number of test cases.

Each test case consists of two lines.

The first line of each test case contains two integers n and k (1 ≤ k ≤ n ≤ 100) — the length of the array and the number in the statement above.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ ai ≤ 10^9)  — the array itself.

Output
For each test case, print the maximum score you can get, one per line.

Input:
5
3 2
5 6 0
1 1
7
5 3
7 0 4 0 4
4 2
2 7 3 4
3 3
1000000000 1000000000 999999997

Output:
11
7
15
10
2999999997
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    groups = [0] * k
    tempIdx = 0
    for num in arr:
        if(tempIdx >= k):
            tempIdx = 0
        if(num > groups[tempIdx]):
            groups[tempIdx] = num
        tempIdx += 1
    ans = sum(groups)
    print(ans)