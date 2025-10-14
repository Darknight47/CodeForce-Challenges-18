"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1765/B -----------------------------------

Recently, Mishka started noticing that his keyboard malfunctions — maybe it's because he was playing rhythm games too much. 
Empirically, Mishka has found out that every other time he presses a key, it is registered as if the key was pressed twice. 
For example, if Mishka types text, the first time he presses a key, exactly one letter is printed; 
the second time he presses a key, two same letters are printed; the third time he presses a key, one letter is printed; 
the fourth time he presses a key, two same letters are printed, and so on. Note that the number of times a key was pressed is counted for the whole keyboard, not for each key separately. 
For example, if Mishka tries to type the word osu, it will be printed on the screen as ossu.

You are given a word consisting of n lowercase Latin letters. You have to determine if it can be printed on Mishka's keyboard or not. 
You may assume that Mishka cannot delete letters from the word, and every time he presses a key, the new letter (or letters) is appended to the end of the word.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of the test case contains one integer n (1 ≤ n ≤ 100) — the length of the word.

The second line of the test case contains a string s consisting of n lowercase Latin letters — the word that should be checked.

Output
For each test case, print YES if the word s can be printed on Mishka's keyboard, and NO otherwise.

Input:
4
4
ossu
2
aa
6
addonn
3
qwe

Output:
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    ok = True
    idx = 0
    double = False
    while True:
        if(idx >= sze):
            break
        if(double):
            if(idx + 1 < sze):
                if(s[idx] == s[idx + 1]):
                    idx += 2
                else:
                    ok = False
                    break
            else:
                ok = False
                break
            double = False
        else:
            idx += 1
            double = True
    print("YES" if ok else "NO")