"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1672/A ----------------------------------------------

There are n logs, the i-th log has a length of ai meters. Since chopping logs is tiring work, errorgorn and maomao90 have decided to play a game.

errorgorn and maomao90 will take turns chopping the logs with errorgorn chopping first. On his turn, the player will pick a log and chop it into 2 pieces. 
If the length of the chosen log is x, and the lengths of the resulting pieces are y and z, then y and z have to be positive integers, and x=y+z must hold. 
For example, you can chop a log of length 3 into logs of lengths 2 and 1, but not into logs of lengths 3 and 0, 2 and 2, or 1.5 and 1.5.

The player who is unable to make a chop will be the loser. Assuming that both errorgorn and maomao90 play optimally, who will be the winner?

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50)  — the number of logs.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 50)  — the lengths of the logs.

Note that there is no bound on the sum of n over all test cases.

Output
For each test case, print "errorgorn" if errorgorn wins or "maomao90" if maomao90 wins. (Output without quotes).

Input:
2
4
2 4 2 1
1
1

Output:
errorgorn
maomao90
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    evens = sum(1 for x in arr if x % 2 == 0)
    print("errorgorn" if evens % 2 == 1 else "maomao90")