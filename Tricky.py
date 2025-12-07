"""

------------------------------------------------ Link for the challenge: https://codeforces.com/contest/912/problem/A ------------------------------------------------

During the winter holidays, the demand for Christmas balls is exceptionally high. Since it's already 2018, the advances in alchemy allow easy and efficient ball creation by utilizing magic crystals.

Grisha needs to obtain some yellow, green and blue balls. It's known that to produce a yellow ball one needs two yellow crystals, green — one yellow and one blue, 
and for a blue ball, three blue crystals are enough.

Right now there are A yellow and B blue crystals in Grisha's disposal. Find out how many additional crystals he should acquire in order to produce the required number of balls.

Input
The first line features two integers A and B (0 ≤ A, B ≤ 109), denoting the number of yellow and blue crystals respectively at Grisha's disposal.

The next line contains three integers x, y and z (0 ≤ x, y, z ≤ 109) — the respective amounts of yellow, green and blue balls to be obtained.

Output
Print a single integer — the minimum number of crystals that Grisha should acquire in addition.

Input:
4 3
2 1 1

Output:
2
"""
yellowCrystals, blueCrystals = map(int, input().split())
reqYellows, reqGreens, reqBlues = map(int, input().split())
#  a yellow ball ->  two yellow crystals 
# green ball —> one yellow and one blue
#  blue ball -> three blue crystals are enough.
extraCrystalsNeeded = 0

if(reqYellows * 2 > yellowCrystals):
    extraCrystalsNeeded += reqYellows * 2 - yellowCrystals
    yellowCrystals = 0
else:
    yellowCrystals -= reqYellows * 2
if(reqBlues * 3 > blueCrystals):
    extraCrystalsNeeded += reqBlues * 3 - blueCrystals
    blueCrystals = 0
else:
    blueCrystals -= reqBlues * 3
if(reqGreens > min(yellowCrystals, blueCrystals)):
    diff1 = reqGreens - yellowCrystals
    diff2 = reqGreens - blueCrystals
    if(diff1 > 0):
        extraCrystalsNeeded += diff1
    if(diff2 > 0):
        extraCrystalsNeeded += diff2
print(extraCrystalsNeeded)