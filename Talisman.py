"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1688/B -------------------------------------------

Patchouli is making a magical talisman. She initially has n magical tokens. Their magical power can be represented with positive integers a1,a2,…,an.

Patchouli may perform the following two operations on the tokens.

Fusion: Patchouli chooses two tokens, removes them, and creates a new token with magical power equal to the sum of the two chosen tokens.
Reduction: Patchouli chooses a token with an even value of magical power x, removes it and creates a new token with magical power equal to x2.
Tokens are more effective when their magical powers are odd values. Please help Patchouli to find the minimum number of operations she needs to make magical powers of all tokens odd values.

Input
Each test contains multiple test cases.

The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. The description of the test cases follows.

For each test case, the first line contains one integer n (1 ≤ n ≤ 2⋅10^5) — the initial number of tokens.

The second line contains n intergers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the initial magical power of the n tokens.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print a single integer — the minimum number of operations Patchouli needs to make all tokens have an odd value of magical power.

It can be shown that under such restrictions the required sequence of operations exists.

Input:
4
2
1 9
3
1 1 2
3
2 4 8
3
1049600 33792 1280

Output:
0
1
3
10
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    evens = []
    odds = []
    trailingZeros = 30
    for num in arr:
        if(num % 2 == 0):
            temp = (num & -num).bit_length() - 1
            if(temp < trailingZeros):
                trailingZeros = temp
            evens.append(num)
        else:
            odds.append(num)
    if(len(odds) > 0):
        print(len(evens))
    else:
        ans = trailingZeros + len(evens) - 1
        print(ans)