"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/764/A -----------------------------------------

Comrade Dujikov is busy choosing artists for Timofey's birthday and is recieving calls from Taymyr from Ilia-alpinist.

Ilia-alpinist calls every n minutes, i.e. in minutes n, 2n, 3n and so on. Artists come to the comrade every m minutes, i.e. in minutes m, 2m, 3m and so on. 
The day is z minutes long, i.e. the day consists of minutes 1, 2, ..., z. How many artists should be killed so that there are no artists in the room when Ilia calls? 
Consider that a call and a talk with an artist take exactly one minute.

Input
The only string contains three integers — n, m and z (1 ≤ n, m, z ≤ 10^4).

Output
Print single integer — the minimum number of artists that should be killed so that there are no artists in the room when Ilia calls.

Input:
1 1 10

Output:
10
"""
import math
n, m, z = map(int, input().split())
# LCM for “simultaneous multiples” problems.
lcm = (n * m) // math.gcd(n, m)
ans = z // lcm
print(ans)