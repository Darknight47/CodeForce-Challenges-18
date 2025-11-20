"""


-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1798/A ------------------------------

You are given two arrays a1,a2,…,an and b1,b2,…,bn.

In one operation, you can choose any integer i from 1 to n and swap the numbers ai and bi.

Determine whether, after using any (possibly zero) number of operations, the following two conditions can be satisfied simultaneously:

an=max(a1,a2,…,an),
bn=max(b1,b2,…,bn).

Here max(c1,c2,…,ck) denotes the maximum number among c1,c2,…,ck. For example, max(3,5,4)=5, max(1,7,7)=7, max(6,2)=6.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the arrays.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 100) — elements of the first array.

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 100) — elements of the second array.

Output
For each test case, print "Yes" if after using any (possibly zero) number of operations the conditions described above are satisfied. Otherwise, print "No".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
7
3
7 9 7
7 6 9
4
10 10 15 15
10 16 15 15
2
100 99
99 100
1
1
1
9
1 2 3 4 5 6 7 8 9
9 9 9 9 9 9 6 6 6
7
1 1 2 2 1 1 2
1 2 1 2 1 2 1
2
30 4
5 30

Output:
Yes
No
Yes
Yes
Yes
No
No
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    for i in range(sze):
        a = arr[i]
        b = brr[i]
        if(a < b):
            arr[i] = b
            brr[i] = a
    maxArr = max(arr)
    maxBrr = max(brr)
    if(maxArr == arr[-1] and maxBrr == brr[-1]):
        print("YES")
    else:
        print("NO")