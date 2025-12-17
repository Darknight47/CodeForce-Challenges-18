"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/851/A ----------------------------------------

Arpa is researching the Mexican wave.

There are n spectators in the stadium, labeled from 1 to n. They start the Mexican wave at time 0.

At time 1, the first spectator stands.
At time 2, the second spectator stands.
...
At time k, the k-th spectator stands.
At time k + 1, the (k + 1)-th spectator stands and the first spectator sits.
At time k + 2, the (k + 2)-th spectator stands and the second spectator sits.
...
At time n, the n-th spectator stands and the (n - k)-th spectator sits.
At time n + 1, the (n + 1 - k)-th spectator sits.
...
At time n + k, the n-th spectator sits.
Arpa wants to know how many spectators are standing at time t.

Input
The first line contains three integers n, k, t (1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, 1 ≤ t < n + k).

Output
Print single integer: how many spectators are standing at time t.

Input:
10 5 3

Output:
3
"""
n, k, t = map(int, input().split())
cycle = n + k
tt = t % cycle
# Growth phase
if(0 <= tt <= k):
    print(tt)
elif(k < tt <= n): # Stable phase
    print(k)
elif(n < tt <= n + k): # Decline phase   
    print(n + k - tt)