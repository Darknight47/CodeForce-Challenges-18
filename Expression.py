"""

--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2038/N ---------------------------------------------

An expression is a string consisting of three characters, where the first and the last characters are digits (from 0 to 9), and the middle character is a comparison symbol (<, = or >).

An expression is true if the comparison symbol matches the digits (for example, if the first digit is strictly less than the last digit, the comparison symbol should be <).

For example, the expressions 1<3, 4>2, 0=0 are true, while 5>5, 7<3 are not.

You are given a string s, which is an expression. Change as few characters as possible so that s becomes a true expression. Note that if s is already true, you should leave it as it is.

Input
The first line contains one integer t (1 ≤ t ≤ 300) — the number of test cases.

Each test case consists of one line containing the string s (|s|=3, the first and the last characters of s are digits, the second character is a comparison symbol).

Output
For each test case, print a string consisting of 3 characters — a true expression which can be obtained by changing as few characters as possible in s. 
If there are multiple answers, print any of them.

Input:
5
3<7
3>7
8=9
0=0
5<3

Output:
3<7
8>7
8<9
0=0
0<3
"""
def exp_checker(exp):
    lessThan = False
    biggerThan = False
    equals = False
    if(exp[1] == '<'):
        lessThan = True
    elif(exp[1] == '>'):
        biggerThan = True
    elif(exp[1] == '='):
        equals = True
    left = int(exp[0])
    right = int(exp[2])
    if(left < right and lessThan):
        return True
    elif(left > right and biggerThan):
        return True
    elif(left == right and equals):
        return True
    return False

cases = int(input())
for _ in range(cases):
    exp = input()
    check = exp_checker(exp)
    if(check):
        print(exp)
    else:
        temp = ['>', '<', '=']
        for ex in temp:
            exp = exp[0] + ex + exp[2]
            check = exp_checker(exp)
            if(check):
                print(exp)
                break