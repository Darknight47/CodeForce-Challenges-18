"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2156/A ----------------------------

Hao and Alex are good friends. After winning a coding competition together, they received a huge pizza as their prize.

Initially, they are given n slices of pizza. Each day, the following process takes place:

If there are at most 2 slices remaining, Alex eats all of them.
Otherwise, let m be the current number of slices (m≥3). 
Hao splits them into three groups of sizes m1, m2, and m3 such that:
m1+m2+m3=m and 1≤m1≤m2≤m3.

Then:
Hao eats m1 slices (the smallest group).
Alex eats m2 slices (the middle group).
The remaining m3 slices (the largest group) are carried over to the next day.
Your task is to determine the maximum total number of slices Hao can eat if he always chooses the partition optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first and only line of each test case contains a single integer n (3 ≤ n ≤ 10^9) — the initial number of pizza slices.

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, output a single integer representing the maximum total number of slices Hao can eat.

Input:
3
8
4
3

Output:
3
1
1
"""
# def split_three(total: int):
#     q, r = divmod(total, 3)
#     if r == 0:
#         return (q, q, q)
#     elif r == 1:
#         return (q, q, q + 1)
#     else:  # r == 2
#         return (q, q + 1, q + 1)
cases = int(input())
for _ in range(cases):
    num = int(input())
    ans = (num - 1) // 2
    print(ans)