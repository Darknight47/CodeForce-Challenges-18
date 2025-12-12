"""

------------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2176/A ----------------------------------------------

Given an array a1,a2,…,an. In one operation, you can choose a pair of indices i,j such that 1 ≤ i < j ≤ n, ai > aj, and remove the element at index j from the array. 
After that, the size of the array will decrease by 1, and the relative order of the elements will not change.

Determine the maximum number of operations that can be performed on the array if they are applied optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 50). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the size of the initial array.

The second line of each test case contains n natural numbers a1,a2,…,an (1 ≤ ai ≤ n).

Output
For each test case, output the maximum number of operations that you can perform on the given array.


Input:
5
3
3 2 1
3
1 2 3
3
3 3 3
5
3 1 4 5 2
1
1

Output:
2
0
0
2
0
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    lastIdx = sze 
    ans = 0
    while lastIdx > 0:
        lastNum = arr[lastIdx - 1]
        for i in range(0, lastIdx - 1):
            temp = arr[i]
            if(temp > lastNum):
                ans += 1
                break
        lastIdx -= 1
    print(ans)