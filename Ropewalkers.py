"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1185/A ------------------------------------------

Polycarp decided to relax on his weekend and visited to the performance of famous ropewalkers: Agafon, Boniface and Konrad.

The rope is straight and infinite in both directions. 
At the beginning of the performance, Agafon, Boniface and Konrad are located in positions a, b and c respectively. At the end of the performance, the distance between each pair of ropewalkers was at least d.

Ropewalkers can walk on the rope. In one second, only one ropewalker can change his position. Every ropewalker can change his position exactly by 1
(i. e. shift by 1 to the left or right direction on the rope). Agafon, Boniface and Konrad can not move at the same time (Only one of them can move at each moment). 
Ropewalkers can be at the same positions at the same time and can "walk past each other".

You should find the minimum duration (in seconds) of the performance. 
In other words, find the minimum number of seconds needed so that the distance between each pair of ropewalkers can be greater or equal to d.

Ropewalkers can walk to negative coordinates, due to the rope is infinite to both sides.

Input
The only line of the input contains four integers a, b, c, d (1 ≤ a, b, c, d ≤ 10^9). 
It is possible that any two (or all three) ropewalkers are in the same position at the beginning of the performance.

Output
Output one integer — the minimum duration (in seconds) of the performance.

Input:
5 2 6 3

Output:
2
"""
a, b, c, d = map(int, input().split())
arr = sorted([a, b, c])
a = arr[0]
b = arr[1]
c = arr[2]
ans = 0
diff1 = abs(a - b)
if(diff1 < d):
    tmp = d - diff1
    ans += tmp
    a -= tmp
diff2 = abs(b - c)
if(diff2 < d):
    tmp = d - diff2
    ans += tmp
    c += tmp
diff3 = c - a
if(diff3 < d):
    tmp = d - diff3
    ans += tmp
    c += tmp
print(ans)