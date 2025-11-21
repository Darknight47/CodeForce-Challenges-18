"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2078/A ------------------------------

You are given an array a of length n, and must perform the following operation until the length of a becomes 1.

Choose a positive integer k<|a| such that |a|k is an integer. Split a into k subsequences∗ s1,s2,…,sk such that:

Each element of a belongs to exactly one subsequence. The length of every subsequence is equal.
After this, replace a=[avg(s1),avg(s2),…,avg(sk)], 
where avg(s)=∑|s|i=1si|s| is the average of all the values in the subsequence. For example, avg([1,2,1,1])=54=1.25.

Your task is to determine whether there exists a sequence of operations such that after all operations, a=[x].

∗ A sequence x is a subsequence of a sequence y if x can be obtained from y by the deletion of several (possibly, zero or all) elements.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains two integers n, x (1 ≤ n, x ≤ 100) — the length of the array a and the final desired value.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 100) — the array a.

Output
For each test case, output "YES'" (without quotes) if there exists such a sequence of operations, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" will be recognized as a positive response).

Input:
4
1 3
3
4 9
7 11 2 5
6 9
1 9 14 12 10 8
10 10
10 10 10 10 10 10 10 10 10 10

Output:
YES
NO
YES
YES
"""
cases = int(input())
for i in range(cases):
    n, x = map(int, input().split())
    arrSum = sum(list(map(int, input().split())))
    ans = arrSum // n
    #if sum(a) == n*x:
    if(arrSum == x * n):
        print("YES")
    else:
        print("NO")