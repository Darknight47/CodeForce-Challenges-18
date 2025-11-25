"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1697/B ------------------------------

The store sells n items, the price of the i-th item is pi. 
The store's management is going to hold a promotion: if a customer purchases at least x items, y cheapest of them are free.

The management has not yet decided on the exact values of x and y. 
Therefore, they ask you to process q queries: for the given values of x and y, determine the maximum total value of items received for free, if a customer makes one purchase.

Note that all queries are independent; they don't affect the store's stock.

Input
The first line contains two integers n and q (1 ≤ n, q ≤ 2⋅10^5) — the number of items in the store and the number of queries, respectively.

The second line contains n integers p1,p2,…,pn (1 ≤ pi ≤ 10^6), where pi — the price of the i-th item.

The following q lines contain two integers xi and yi each (1 ≤ yi ≤ xi ≤ n) — the values of the parameters x and y in the i-th query.

Output
For each query, print a single integer — the maximum total value of items received for free for one purchase.

Input:
5 3
5 3 1 5 2
3 2
1 1
5 3

Output:
8
5
6
"""
n, q = map(int, input().split())
arr = sorted(list(map(int, input().split())))
# Build prefix sums
prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

for _ in range(q):
    x, y = map(int, input().split())
    ans = prefix[n-x+y] - prefix[n-x]
    print(ans)