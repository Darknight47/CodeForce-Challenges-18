"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2098/A --------------------------------

We call a phone number a beautiful if it is a string of 10 digits, where the i-th digit from the left is at least 10−i. 
That is, the first digit must be at least 9, the second at least 8, …, with the last digit being at least 0.

For example, 9988776655 is a beautiful phone number, while 9099999999 is not, since the second digit, which is 0, is less than 8.

Vadim has a beautiful phone number. He wants to rearrange its digits in such a way that the result is the smallest possible beautiful phone number. Help Vadim solve this problem.

Please note that the phone numbers are compared as integers.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains a single string s of length 10, consisting of digits. It is guaranteed that s is a beautiful phone number.

Output
For each test case, output a single string of length 10 — the smallest possible beautiful phone number that Vadim can obtain.

Input:
4
9999999999
9988776655
9988776650
9899999999

Output:
9999999999
9876556789
9876567890
9899999999
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    nums = int(input())
    diction = {}
    while nums > 0:
        temp = nums % 10
        if(temp in diction):
            diction[temp] += 1
        else:
            diction[temp] = 1
        nums //= 10
    keys = sorted(diction.keys())
    result = []
    # Work on a copy so we don't mutate original
    counts = diction.copy()
    
    for i in range(10):
        req = 9 - i  # minimum required digit
        # find smallest available digit >= req
        candidate = None
        for d in range(req, 10):  # search upwards
            if counts.get(d, 0) > 0:
                candidate = d
                break
        result.append(candidate)
        counts[candidate] -= 1
    
    print(''.join(str(d) for d in result))