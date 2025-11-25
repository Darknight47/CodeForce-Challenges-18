"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1657/B ------------------------------------

You are given four integers n, B, x and y. You should build a sequence a0,a1,a2,…,an where a0=0 and for each i ≥ 1 you can choose:

either ai=ai−1+x
or ai=ai−1−y.

Your goal is to build such a sequence a that ai ≤ B for all i and ∑i=0nai is maximum possible.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Next t cases follow.

The first and only line of each test case contains four integers n, B, x and y (1 ≤ n ≤ 2⋅10^5; 1 ≤ B, x, y ≤ 10^9).

It's guaranteed that the total sum of n doesn't exceed 2⋅10^5.

Output
For each test case, print one integer — the maximum possible ∑i=0nai.

Input:
3
5 100 1 30
7 1000000000 1000000000 1000000000
4 1 7 3

Output:
15
4000000000
-10
"""
cases = int(input())
for _ in range(cases):
    n, B, x, y = map(int, input().split())
    current = 0
    ans = 0
    for i in range(n):
        temp1 = current + x
        temp2 = current - y
        if(temp1 <= B and temp2 <= B):
            tempMax = max(temp1, temp2)
            current = tempMax
        else:
            if(temp1 <= B and temp2 > B):
                current = temp1
            else:
                current = temp2
        ans += current
    print(ans)