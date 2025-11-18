"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2036/B -----------------------------------------

Arseniy came up with another business plan — to sell soda from a vending machine! For this, he purchased a machine with n shelves, as well as k bottles, 
where the i-th bottle is characterized by the brand index bi and the cost ci.

You can place any number of bottles on each shelf, but all bottles on the same shelf must be of the same brand.

Arseniy knows that all the bottles he puts on the shelves of the machine will be sold. Therefore, he asked you to calculate the maximum amount he can earn.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and k (1 ≤ n, k ≤ 2⋅10^5), where n is the number of shelves in the machine, and k is the number of bottles available to Arseniy.

The next k lines contain two integers bi and ci (1 ≤ bi ≤ k, 1 ≤ ci ≤ 1000) — the brand and cost of the i-th bottle.

It is also guaranteed that the sum of n across all test cases does not exceed 2⋅10^5 and that the sum of k across all test cases also does not exceed 2⋅10^5.

Output
For each test case, output one integer — the maximum amount that Arseniy can earn.

Input:
4
3 3
2 6
2 7
1 15
1 3
2 6
2 7
1 15
6 2
1 7
2 5
190000 1
1 1000

Output:
28
15
12
1000
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    brand_cost = [0] * (k + 1)   # brand indices are up to k (not n)

    for _ in range(k):
        b, c = map(int, input().split())
        brand_cost[b] += c      # accumulate directly

    brand_cost.sort(reverse=True)
    print(sum(brand_cost[:n]))  # sum top n brand