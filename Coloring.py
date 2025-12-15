"""

-------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1408/A ------------------------------------------------

You are given three sequences: a1,a2,…,an; b1,b2,…,bn; c1,c2,…,cn.

For each i, ai≠bi, ai≠ci, bi≠ci.

Find a sequence p1,p2,…,pn, that satisfy the following conditions:

pi∈{ai,bi,ci}
pi≠p(i mod n) + 1.

In other words, for each element, you need to choose one of the three possible values, such that no two adjacent elements 
(where we consider elements i,i+1 adjacent for i<n and also elements 1 and n) will have equal value.

It can be proved that in the given constraints solution always exists. You don't need to minimize/maximize anything, you need to find any proper sequence.

Input
The first line of input contains one integer t (1 ≤ t ≤ 100): the number of test cases.

The first line of each test case contains one integer n (3 ≤ n ≤ 100): the number of elements in the given sequences.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 100).

The third line contains n integers b1,b2,…,bn (1 ≤ bi ≤ 100).

The fourth line contains n integers c1,c2,…,cn (1 ≤ ci ≤ 100).

It is guaranteed that ai≠bi, ai ≠ ci, bi ≠ ci for all i.

Output
For each test case, print n integers: p1,p2,…,pn (pi ∈ {ai,bi,ci}, pi ≠ pi mod n+1).

If there are several solutions, you can print any.

Input:
5
3
1 1 1
2 2 2
3 3 3
4
1 2 1 2
2 1 2 1
3 4 3 4
7
1 3 3 1 1 1 1
2 4 4 3 2 2 4
4 2 2 2 4 4 2
3
1 2 1
2 3 3
3 1 2
10
1 1 1 2 2 2 3 3 3 1
2 2 2 3 3 3 1 1 1 2
3 3 3 1 1 1 2 2 2 3

Output:
1 2 3
1 2 1 2
1 3 4 3 2 4 2
1 3 2
1 2 3 1 2 3 1 2 3 2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = list(map(int, input().split()))
    ans = []
    for i in range(sze - 1):
        if(not ans):
            ans.append(arr[i])
        else:
            temp = ans[-1]
            if(temp != arr[i]):
                ans.append(arr[i])
            elif(temp != brr[i]):
                ans.append(brr[i])
            elif(temp != crr[i]):
                ans.append(crr[i])
    next = ans[0]
    prev = ans[-1]
    if(arr[-1] != next and arr[-1] != prev):
        ans.append(arr[-1])
    elif(brr[-1] != next and brr[-1] != prev):
        ans.append(brr[-1])
    elif(crr[-1] != next and crr[-1] != prev):
        ans.append(crr[-1])
    print(*ans)