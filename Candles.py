"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2145/A ------------------------------------

Monocarp has three nephews. New Year is coming, and Monocarp has n candies that he will gift to his nephews.

To ensure that none of the nephews feels left out, Monokarp wants to give each of the three nephews the same number of candies.

Determine the minimum number of candies that Monocarp needs to buy additionally so that he can give each of the three nephews the same number of candies. 
Note that all n candies that Monocarp initially has will be given to the nephews.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

Each test case consists of one line containing one integer n (1 ≤ n ≤ 100) — the number of candies that Monocarp initially has.

Output 
For each test case, print one integer — the minimum number of candies that Monocarp needs to buy additionally so that he can give each of the three nephews the same number of candies.

Input:
2
7
24

Output:
2
0
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    ans = 0
    while(num % 3 != 0):
        num += 1
        ans += 1
    print(ans)