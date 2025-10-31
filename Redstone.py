"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2133/A --------------------------------------

Steve stumbled upon a collection of n gears, where gear i has ai teeth, and he wants to arrange them into a row.

After he arranges them, Steve will spin the leftmost gear at a speed of 1 revolution per second. For each of the other gears, let x be the number of teeth it has, 
y be the number of teeth of the gear to its left, and z be the speed the gear to its left spins at. Then, its speed will be yx⋅z revolutions per second.

Steve considers the contraption satisfactory if the rightmost gear spins at a speed of 1 revolution per second. Determine whether Steve can rearrange the gears into a satisfactory contraption.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the number of gears Steve has.

The second line of each test case contains n integers a1,a2,…,an (2 ≤ a(i) ≤ 100) — the number of teeth of each gear.

Output
For each test case, print "YES" if Steve can rearrange the gears in a satisfactory way, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
2
5 5
4
6 3 6 9
2
2 3
7
30 10 12 10 10 9 18
5
2 4 8 16 32

Output:
YES
YES
NO
YES
NO
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    ok = False
    for key, val in counts.items():
        if(val >= 2):
            ok = True
            break
    print("YES" if ok else "NO")