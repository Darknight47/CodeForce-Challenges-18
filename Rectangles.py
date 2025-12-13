"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2120/A -----------------------------------------------

Aryan is an ardent lover of squares but a hater of rectangles (Yes, he knows all squares are rectangles). 
But Harshith likes to mess with Aryan. Harshith gives Aryan three rectangles of sizes l1×b1, l2×b2, and l3×b3 such that l3≤l2≤l1 and b3≤b2≤b1. 
Aryan, in order to defeat Harshith, decides to arrange these three rectangles to form a square such that no two rectangles overlap and the rectangles are aligned along edges. 
Rotating rectangles is not allowed. Help Aryan determine if he can defeat Harshith.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

Each test case contains a single line with 6 space-separated integers l1,b1,l2,b2,l3, and b3 (1 ≤ l3 ≤ l2 ≤ l1 ≤ 100, 1 ≤ b3 ≤ b2 ≤ b1 ≤ 100) — the dimensions of the three rectangles.

Output
For each testcase, print "YES" if the rectangles can be arranged to form a square; otherwise, "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
100 100 10 10 1 1
5 3 5 1 5 1
2 3 1 2 1 1
8 5 3 5 3 3
3 3 3 3 2 1

Output:
NO
YES
YES
NO
NO
"""
import math
def can_form_square(l1, b1, l2, b2, l3, b3):
    area = l1*b1 + l2*b2 + l3*b3
    S = int(math.isqrt(area))
    if S*S != area:
        return False

    # Fit check
    if not (l1 <= S and l2 <= S and l3 <= S and b1 <= S and b2 <= S and b3 <= S):
        return False

    # Case 1: all lengths equal S, breadths sum to S
    if l1 == S and l2 == S and l3 == S and (b1 + b2 + b3 == S):
        return True

    # Case 2: all breadths equal S, lengths sum to S
    if b1 == S and b2 == S and b3 == S and (l1 + l2 + l3 == S):
        return True

    # Case 3: rect1 spans full width; bottom row is two rectangles side-by-side
    if l1 == S and b2 == b3 == (S - b1) and (l2 + l3 == S):
        return True

    # Case 4: rect1 spans full height; right column is two rectangles stacked
    if b1 == S and l2 == l3 == (S - l1) and (b2 + b3 == S):
        return True

    return False

cases = int(input())
for _ in range(cases):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    print("YES" if can_form_square(l1, b1, l2, b2, l3, b3) else "NO")