"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1498/A -----------------------------

The gcdSum of a positive integer is the gcd of that integer with its sum of digits. Formally, gcdSum(x)=gcd(x, sum of digits of x) for a positive integer x. 
gcd(a,b) denotes the greatest common divisor of a and b — the largest integer d such that both integers a and b are divisible by d.

For example: gcdSum(762) = gcd(762,7+6+2) = gcd(762,15) = 3.

Given an integer n, find the smallest integer x≥n such that gcdSum(x) > 1.

Input
The first line of input contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Then t lines follow, each containing a single integer n (1 ≤ n ≤ 10^18).

All test cases in one test are different.

Output
Output t lines, where the i-th line is a single integer containing the answer to the i-th test case.

Input:
3
11
31
75

Output:
12
33
75
"""
import math 
cases = int(input())
for _ in range(cases):
    num = int(input())
    while True:
        numCpy = num
        sumDigits = 0
        while(numCpy > 0):
            dig = numCpy % 10
            sumDigits += dig
            numCpy //= 10
        ans = math.gcd(num, sumDigits)
        if(ans > 1):
            print(num)
            break
        num += 1