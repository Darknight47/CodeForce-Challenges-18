"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2022/A ---------------------------------------

There are n families travelling to Pénjamo to witness Mexico's largest-ever "walking a chicken on a leash" marathon. The i-th family has ai family members. 
All families will travel using a single bus consisting of r rows with 2 seats each.

A person is considered happy if:

Another family member is seated in the same row as them, or
They are sitting alone in their row (with an empty seat next to them).
Determine the maximum number of happy people in an optimal seating arrangement. Note that everyone must be seated in the bus.

It is guaranteed that all family members will fit on the bus. Formally, it is guaranteed that ∑i=1nai≤2r.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The first line of each test case contains two integers n and r (1 ≤ n ≤ 100; 1 ≤ r ≤ 500) — the number of families and the number of rows in the bus.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10) — the number of family members in each family.

Output
For each test case, output the maximum number of happy people in an optimal seating arrangement.

Input:
4
3 3
2 3 1
3 3
2 2 2
4 5
1 1 2 2
4 5
3 1 1 3

Output:
4
6
6
6
"""
cases = int(input())
for _ in range(cases):
    n, r = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    leftAlons = 0
    usedRows = 0
    for i in range(n):
        family = arr[i]
        requiredRow, leftAlone = divmod(family, 2)
        usedRows += requiredRow
        leftAlons += leftAlone
    ans = usedRows * 2
    leftRows = r - usedRows
    if(leftRows >= leftAlons):
        ans += leftAlons
    else:
        temp = 2 * leftRows - leftAlons
        ans += temp
    print(ans)