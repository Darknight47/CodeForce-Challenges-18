"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/897/A -----------------------------------------------

Willem is taking the girl to the highest building in island No.28, however, neither of them knows how to get there.

Willem asks his friend, Grick for directions, Grick helped them, and gave them a task.

Although the girl wants to help, Willem insists on doing it by himself.

Grick gave Willem a string of length n.

Willem needs to do m operations, each operation has four parameters l, r, c1, c2, which means that all symbols c1 in range [l, r] (from l-th to r-th, including l and r) are changed into c2. String is 1-indexed.

Grick wants to know the final string after all the m operations.

Input
The first line contains two integers n and m (1 ≤ n, m ≤ 100).

The second line contains a string s of length n, consisting of lowercase English letters.

Each of the next m lines contains four parameters l, r, c1, c2 (1 ≤ l ≤ r ≤ n, c1, c2 are lowercase English letters), separated by space.

Output
Output string s after performing m operations described above.

Input:
3 1
ioi
1 1 i n

Output:
noi
"""
n, m = map(int, input().split())
s = list(input())
for _ in range(m):
    l, r, c1, c2 = input().split()
    l = int(l) - 1
    r = int(r) 
    for i in range(l, r):
        if(s[i] == c1):
            s[i] = c2
print("".join(s))