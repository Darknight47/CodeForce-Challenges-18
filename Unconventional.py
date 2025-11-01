"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2149/B ---------------------------------------

A popular reality show Unconventional Pairs has been launched in the city. According to the rules of the show, participants are paired in an unusual way: 
with an even number of people, all participants must be in pairs.

Petya has an array of n integers a1,a2,…,an. It is known that n is even. Petya must divide the participants (numbers) into exactly n2 pairs (ap1,aq1),(ap2,aq2),…(apn2,aqn2). 
Each index can be included in no more than one pair.

For a pair (x,y), its difference is defined as |x−y|. Petya wants to form unconventional pairs such that the maximum difference among all pairs is minimized.

Determine the minimum possible value of this maximum difference.

Input
Each test consists of several test cases.

The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains one even number n (2 ≤ n ≤ 2⋅10^5) — the length of the array a.

The second line contains n integers a1,a2,…,an (−10^ 9 ≤ ai ≤ 10^9)— the elements of the array a.

It is guaranteed that the sum of the values of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single number — the minimum possible maximum difference between the elements in pairs.

Input:
5
2
1 2
4
10 1 2 9
6
3 8 9 3 3 2
8
5 5 5 5 5 5 5 5
4
-5 -1 2 6

Output:
1
1
1
0
4
"""
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    maxDiff = -math.inf
    for i in range(0, sze, 2):
        temp = abs(arr[i] - arr[i + 1])
        if(temp > maxDiff):
            maxDiff = temp
    print(maxDiff)