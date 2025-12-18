"""

------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1054/A --------------------------------------------

Masha lives in a multi-storey building, where floors are numbered with positive integers. 
Two floors are called adjacent if their numbers differ by one. Masha decided to visit Egor. Masha lives on the floor x, Egor on the floor y (not on the same floor with Masha).

The house has a staircase and an elevator. If Masha uses the stairs, it takes t1 seconds for her to walk between adjacent floors (in each direction). 
The elevator passes between adjacent floors (in each way) in t2 seconds. The elevator moves with doors closed. 
The elevator spends t3 seconds to open or close the doors. We can assume that time is not spent on any action except moving between adjacent floors and waiting for the doors to open or close. 
If Masha uses the elevator, it immediately goes directly to the desired floor.

Coming out of the apartment on her floor, Masha noticed that the elevator is now on the floor z and has closed doors. Now she has to choose whether to use the stairs or use the elevator.

If the time that Masha needs to get to the Egor's floor by the stairs is strictly less than the time it will take her using the elevator, then she will use the stairs, otherwise she will choose the elevator.

Help Mary to understand whether to use the elevator or the stairs.

Input
The only line contains six integers x, y, z, t1, t2, t3 (1≤x,y,z,t1,t2,t3≤1000) — the floor Masha is at, the floor Masha wants to get to, the floor the elevator is located on, 
the time it takes Masha to pass between two floors by stairs, 
the time it takes the elevator to pass between two floors and the time it takes for the elevator to close or open the doors.

It is guaranteed that x≠y.

Output
If the time it will take to use the elevator is not greater than the time it will take to use the stairs, print «YES» (without quotes), otherwise print «NO> (without quotes).

You can print each letter in any case (upper or lower).

Input:
5 1 4 4 2 1

Output:
YES
"""
x, y, elevatorPos, timeWithStaris, timeWithElev, opening_closing = map(int, input().split())
distance = abs(x - y)
time_taken_with_stairs = distance * timeWithStaris

elevDistance = abs(x- elevatorPos)
elev_time_taken_to_x = elevDistance * timeWithElev
loading_time = elev_time_taken_to_x + opening_closing + opening_closing
moving_time_with_elev = distance * timeWithElev
total_time_with_elev = loading_time + moving_time_with_elev + opening_closing

if(time_taken_with_stairs < total_time_with_elev):
    print("NO")
else:
    print("YES")