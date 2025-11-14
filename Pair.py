"""

--------------------------------------- Link for the challenge: https://codeforces.com/contest/2164/problem/B ---------------------------------

You are given a strictly increasing sequence of positive integers a1 < a2 < … < an. 
Find two distinct elements x and y from the sequence such that x<y and y mod x is even, or determine that no such pair exists.

p mod q denotes the remainder from dividing p by q.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 2⋅10^4). The description of the test cases follows.

The first line of each test case contains one integer n (2 ≤ n ≤ 10^5) — the length of the sequence.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a1 < … < an ≤ 10^9) — the given sequence.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case:

If no such pair exists, output -1.
Otherwise, output two integers x and y — the elements that satisfy the condition.
If there are multiple valid pairs, you may output any of them.

Input:
4
5
1 3 4 5 6
6
2 3 5 7 11 13
4
2 3 13 37
3
17 117 1117

Output:
3 5
3 11
-1
17 1117
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    num_set = set(arr)
    max_val = arr[-1]
    ok = False
    for i in range(sze):
        for j in range(i + 1, sze):
            small, large = arr[i], arr[j]
            temp = large % small
            if temp % 2 == 0:
                ok =  True
                print(small, large)
                break
        if(ok):
            break
    if(not ok):
        print(-1)