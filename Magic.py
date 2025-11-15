"""
--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2167/C ------------------------------------------

Isamatdin has n toys arranged in a row. The i-th toy has an integer ai. 
He wanted to sort them because otherwise, his mother would scold him.

However, Isamatdin never liked arranging toys in order, so his friend JahonaliX gave him a magic wand to help. Unfortunately, JahonaliX made a small mistake while creating the wand.

But Isamatdin couldn't wait any longer and decided to use the broken wand anyway. 
The wand can only swap two toys if their integers have different parity (one is even, the other is odd). In other words, you can swap toys in positions (i,j)
only if ai mod 2 ≠ aj mod 2, where mod — is the remainder of integer division.

Now he wants to know the lexicographically smallest∗ arrangement he can achieve using this broken wand.

∗ A sequence p is lexicographically smaller than a sequence q if there exists an index i such that pj = qj for all j < i, and pi < qi.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of toys.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the integers of the toys.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output n integers — the lexicographically smallest sequence that can be obtained using the described operation.

Input:
7
4
2 3 1 4
5
3 2 1 3 4
4
3 7 5 1
2
1000000000 2
3
1 3 5
5
2 5 3 1 7
4
2 4 8 6

Output:
1 2 3 4 
1 2 3 3 4 
3 7 5 1 
1000000000 2 
1 3 5 
1 2 3 5 7 
2 4 8 6 
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    odd = even = False
    for num in arr:
        if(num % 2 == 0):
            odd = True
        else:
            even = True
        if(odd and even):
            break
    if(odd and even):
        ans = sorted(arr)
        print(*ans)
    else:
        print(*arr)