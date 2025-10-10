"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1504/A -----------------------------------


A palindrome is a string that reads the same backward as forward. For example, the strings "z", "aaa", "aba", and "abccba" are palindromes, but "codeforces" and "ab" are not. 
You hate palindromes because they give you déjà vu.

There is a string s. You must insert exactly one character 'a' somewhere in s. 
If it is possible to create a string that is not a palindrome, you should find one example. Otherwise, you should report that it is impossible.

For example, suppose s= "cbabc". By inserting an 'a', you can create "acbabc", "cababc", "cbaabc", "cbabac", or "cbabca". However "cbaabc" is a palindrome, so you must output one of the other options.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains a string s consisting of lowercase English letters.

The total length of all strings does not exceed 3⋅10^5.

Output
For each test case, if there is no solution, output "NO".

Otherwise, output "YES" followed by your constructed string of length |s|+1 on the next line. If there are multiple solutions, you may print any.

You can print each letter of "YES" and "NO" in any case (upper or lower).

Input:
6
cbabc
ab
zza
ba
a
nutforajaroftuna

Output:
YES
cbabac
YES
aab
YES
zaza
YES
baa
NO
YES
nutforajarofatuna
"""
cases = int(input())
for _ in range(cases):
    s = input()
    s1 = 'a' + s
    s2 = s + 'a'
    if s1 != s1[::-1]:
        print("yes")
        print(s1)
    elif s2 != s2[::-1]:
        print("yes")
        print(s2)
    else:
        print("no")