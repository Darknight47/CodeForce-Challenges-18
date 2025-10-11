"""
------------------------------------ Link for the challenge: https://codeforces.com/contest/1998/problem/A ------------------------------------

You are given three integers xc, yc, and k (−100 ≤ xc, yc ≤100, 1 ≤ k ≤ 1000).

You need to find k distinct points (x1,y1), (x2,y2), …, (xk,yk), having integer coordinates, on the 2D coordinate plane such that:

their center∗ is (xc,yc)
−10^9 ≤ xi , yi ≤ 10^9 for all i from 1 to k
It can be proven that at least one set of k distinct points always exists that satisfies these conditions.

∗ The center of k points (x1,y1), (x2,y2), …, (xk,yk) is (x1+x2+…+xkk,y1+y2+…+ykk).

Input
The first line contains t (1 ≤ t ≤ 100) — the number of test cases.

Each test case contains three integers xc, yc, and k (−100 ≤ xc, yc ≤ 100, 1 ≤ k ≤ 1000) — the coordinates of the center and the number of distinct points you must output.

It is guaranteed that the sum of k over all test cases does not exceed 1000.

Output
For each test case, output k lines, the i-th line containing two space separated integers, xi and yi, (−10^9 ≤ xi , yi ≤ 10^9) — denoting the position of the i-th point.

If there are multiple answers, print any of them. It can be shown that a solution always exists under the given constraints.

Input:
4
10 10 1
0 0 3
-5 -8 8
4 -5 3

Output:
10 10
-1 -1
5 -1
-4 2
-6 -7
-5 -7
-4 -7
-4 -8
-4 -9
-5 -9
-6 -9
-6 -8
1000 -1000
-996 995
8 -10
"""
cases = int(input())
for _ in range(cases):
    xc, yc, k = map(int, input().split())
    points = []
    if k % 2 == 1:
        # include the center itself
        points.append((xc, yc))
        half = (k - 1) // 2
        for i in range(1, half + 1):
            points.append((xc + i, yc + i))
            points.append((xc - i, yc - i))
    else:
        half = k // 2
        for i in range(1, half + 1):
            points.append((xc + i, yc + i))
            points.append((xc - i, yc - i))
    for x, y in points:
        print(x, y)