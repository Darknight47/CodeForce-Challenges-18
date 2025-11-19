"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2121/B ------------------------------------------------

You are given a string s of length n, consisting of lowercase letters of the Latin alphabet. Determine whether there exist three non-empty strings a, b, and c such that:

a + b + c = s, meaning the concatenation∗ of strings a, b, and c equals s.
The string b is a substring† of the string a+c, which is the concatenation of strings a and c.
∗ Concatenation of strings a and b is defined as the string a+b=a1a2…apb1b2…bq, where p and q are the lengths of strings a and b, respectively. 
For example, the concatenation of the strings "code" and "forces" is "codeforces".

† A string a is a substring of a string b if a can be obtained from b by the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10^5) — the length of the string s.

The second line of each test case contains the string s of length n, consisting of lowercase letters of the Latin alphabet.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
For each test case, output "Yes" if there exist three non-empty strings a, b, and c that satisfy the conditions, and "No" otherwise.

You may output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.

Input:
12
3
aaa
3
aba
3
aab
4
abca
4
abba
4
aabb
5
abaca
5
abcda
5
abcba
6
abcbbf
6
abcdaa
3
abb

Output:
Yes
No
Yes
No
Yes
Yes
Yes
No
Yes
Yes
Yes
Yes
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    counts = Counter(s)
    ok = False
    for tc, tv in counts.items():
        if(tv >= 3):
            ok = True
            break
        if(tv == 2):
            if(s[0] != tc or s[sze - 1] != tc):
                ok = True
                break
    print("YES" if ok else "NO")