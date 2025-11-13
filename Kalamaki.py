"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2163/A --------------------------------------

Two players, Souvlaki and Kalamaki, are given a sequence a of n integers.

They will play a game that consists of n−1 rounds, which are numbered from 1 to n−1. 
Souvlaki plays on odd-numbered rounds, and Kalamaki on even-numbered rounds.

On the i-th round, a player can choose to take exactly one of the following actions:

Skip his turn and proceed to round i+1 (or finish the game if round i was the last one).
Swap elements ai and ai+1.
Souvlaki wins if after the end of the last round, a is sorted in non-decreasing order. In other words, he wins if ai≤ai+1 holds for every 1 ≤ i < n. Otherwise, Kalamaki wins.

However, Souvlaki does not like losing, so before the start of the game, he may re-order the elements of a 
in anyway he wants. Is it possible for him to do so such that he has a guaranteed winning strategy?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains a single integer, n (3 ≤ n ≤ 100) — the number of integers in a.

The second line contains exactly n integers a1,a2,…,an (1 ≤ ai ≤ n) — where ai represents the i-th element of a.

Output
For each test case, output on a separate line "'YES"' if it is possible for Souvlaki to re-order the elements of a such that he has a guaranteed winning strategy, and "'NO"' otherwise.

You can output the answer in any case (upper or lower). For example, the strings "'yEs"', "'yes"', "'Yes"', and "'YES"' will be recognized as positive responses.

Input:
5
4
4 2 2 1
4
1 1 1 1
5
1 5 1 5 1
3
1 2 3
5
1 3 2 3 5

Output:
YES
YES
YES
NO
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    ok = True
    for i in range(1, sze - 1, 2):
        if(not arr[i] == arr[i + 1]):
            ok = False
            break
        if(i + 2 < sze and not (arr[i + 1] <= arr[i + 2])):
            ok = False
            break
    print("YES" if ok else "NO")