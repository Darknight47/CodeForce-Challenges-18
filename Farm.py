"""

------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2171/A ------------------------------------

Kaori wants to spend the day with Shizuku! However, the zoo is closed, so they are visiting Farmer John's farm instead.

At Farmer John's farm, Shizuku counts n legs. It is known that only chickens and cows live on the farm; a chicken has 2 legs, while a cow has 4.

Count how many different configurations of Farmer John's farm are possible. 
Two configurations are considered different if they contain either a different number of chickens, a different number of cows, or both.

Note that Farmer John's farm may contain zero chickens or zero cows.

Input
The first line contains a single integer t (1 ≤ t ≤ 100)  — the number of test cases.

The only line of each test case contains a single integer n (1 ≤ n ≤ 100).

Output
For each test case, output a single integer, the number of different configurations of Farmer John's farm that are possible.

Input:
5
2
3
4
6
100

Outupt:
1
0
2
2
26
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n % 2 == 1):
        print(0)
    else:
        m = n // 2
        results = []
        # Iterate over possible counts of 4s
        for y in range(m // 2 + 1):
            x = m - 2 * y
            if x >= 0:
                results.append((x, y))  # (number_of_twos, number_of_fours)
        print(len(results))