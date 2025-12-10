"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1413/A -------------------------------------------

Naruto has sneaked into the Orochimaru's lair and is now looking for Sasuke. There are T rooms there. 
Every room has a door into it, each door can be described by the number n of seals on it and their integer energies a1, a2, ..., an. 
All energies ai are nonzero and do not exceed 100 by absolute value. Also, n is even.

In order to open a door, Naruto must find such n seals with integer energies b1, b2, ..., bn that the following equality holds: a1⋅b1+a2⋅b2+...+an⋅bn=0. 
All bi must be nonzero as well as ai are, and also must not exceed 100 by absolute value. Please find required seals for every room there.

Input
The first line contains the only integer T (1 ≤ T ≤ 1000) standing for the number of rooms in the Orochimaru's lair. The other lines contain descriptions of the doors.

Each description starts with the line containing the only even integer n (2 ≤ n ≤ 100) denoting the number of seals.

The following line contains the space separated sequence of nonzero integers a1, a2, ..., an (|ai| ≤ 100, ai ≠ 0) denoting the energies of seals.

Output
For each door print a space separated sequence of nonzero integers b1, b2, ..., bn (|bi| ≤ 100, bi ≠ 0) denoting the seals that can open the door. 
If there are multiple valid answers, print any. It can be proven that at least one answer always exists.

Input:
2
2
1 100
4
1 2 3 6

Output:
-100 1
1 1 1 -1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(0, sze, 2):
        a = arr[i]
        b = arr[i + 1]
        ans.append(b)
        ans.append(-a)
    print(*ans)