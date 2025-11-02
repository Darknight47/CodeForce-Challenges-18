"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2037/B -------------------------------------------

To help you prepare for your upcoming Codeforces contest, Citlali set a grid problem and is trying to give you a n by m grid through your input stream. 
Specifically, your input stream should contain the following:

The first line contains two integers n and m — the dimensions of the grid.
The following n lines contain m integers each — the values of the grid.
However, someone has intercepted your input stream, shuffled all given integers, and put them all on one line! Now, there are k integers all on one line, and you don't know where each integer originally belongs. 
Instead of asking Citlali to resend the input, you decide to determine the values of n and m yourself.

Output any possible value of n and m that Citlali could have provided.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains an integer k (3 ≤ k ≤ 2⋅10^5) — the total number of inputs in your input stream.

The following line of each test case contains k integers a1,a2,…,ak (1 ≤ ai ≤ k) — the shuffled inputs of your input stream. It is guaranteed that n and m are contained within the k integers.

It is guaranteed that the sum of k over all test cases does not exceed 2⋅10^5.

Output
For each test case, output two integers, one possible value of n and m. If multiple possible answers exist, output any.

Input:
5
3
1 1 2
11
3 3 4 5 6 7 8 9 9 10 11
8
8 4 8 3 8 2 8 1
6
2 1 4 5 3 3
8
1 2 6 3 8 5 5 3

Output:
1 1
3 3
2 3
4 1
1 6
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    k = sze - 2
    pairs = []
    for i in range(1, int(k**0.5) + 1):  # check up to sqrt(k)
        if k % i == 0:  # if i divides k evenly
            pairs.append((i, k // i))
    for a, b in pairs:
        if a in arr and b in arr:
            print(a, b)
            break