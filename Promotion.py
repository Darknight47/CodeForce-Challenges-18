"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1793/A ----------------------------------------------

The famous store "Second Food" sells groceries only two days a month. And the prices in each of days differ. You wanted to buy n kilos of potatoes for a month.
You know that on the first day of the month 1 kilo of potatoes costs a coins, and on the second day b coins. In "Second Food" you can buy any integer kilograms of potatoes.

Fortunately, "Second Food" has announced a promotion for potatoes, which is valid only on the first day of the month — for each m kilos of potatoes you buy, you get 1 kilo as a gift! 
In other words, you can get m+1 kilograms by paying for m kilograms.

Find the minimum number of coins that you have to spend to buy at least n kilos of potatoes.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10000). Description of the test cases follows.

The first line of each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) — the prices of 1 kilo of potatoes on the first and second days, respectively.

The second line contains two integers n and m (1 ≤ n, m ≤ 10^9) — the required amount of potatoes to buy and the amount of potatoes to use the promotion.

Output
For each test case print one integer — the minimum number of coins that you have to pay to buy at least n kilos of potatoes.

Input:
5
5 4
3 1
5 4
3 2
3 4
3 5
20 15
10 2
1000000000 900000000
1000000000 8

Output:
9
10
9
135
888888888900000000
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    # Buy everything on the first day
    if(a < b):
        k = n // (m + 1)
        r = n - k * (m + 1)
        x = k * m + r
        cost = a * x
    else: # Buy everything on the second day and check if bundle is better
        p_bundle = (a * m) // (m + 1)
        if(p_bundle >= b):
            cost = b * n
        else:
            k = n // (m + 1)
            r = n - k * (m + 1)
            cost = a * (k * m) + b * r
    print(cost)