"""
-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1236/A --------------------------------------------

Alice is playing with some stones.

Now there are three numbered heaps of stones. The first of them contains a stones, the second of them contains b stones and the third of them contains c stones.

Each time she can do one of two operations:

take one stone from the first heap and two stones from the second heap (this operation can be done only if the first heap contains at least one stone and the second heap contains at least two stones);
take one stone from the second heap and two stones from the third heap (this operation can be done only if the second heap contains at least one stone and the third heap contains at least two stones).

She wants to get the maximum number of stones, but she doesn't know what to do. Initially, she has 0 stones. Can you help her?

Input
The first line contains one integer t (1 ≤ t ≤ 100)  — the number of test cases. Next t lines describe test cases in the following format:

Line contains three non-negative integers a, b and c, separated by spaces (0 ≤ a, b, c ≤ 100) — the number of stones in the first, the second and the third heap, respectively.

In hacks it is allowed to use only one test case in the input, so t=1 should be satisfied.

Output
Print t lines, the answers to the test cases in the same order as in the input. The answer to the test case is the integer  — the maximum possible number of stones that Alice can take after making some operations.

Input:
3
3 4 5
1 0 5
5 3 2

Output:
9
0
6
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    op2 = min(b, c // 2)
    b -= op2
    c -= op2 * 2

    op1 = min(a, b // 2)

    ans = (op1 + op2) * 3 # Each operation gives 3 stones
    print(ans)    