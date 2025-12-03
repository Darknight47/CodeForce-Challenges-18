"""

-------------------------------------------------------- Link for the challenge: https://codeforces.com/contest/908/problem/A ----------------------------------

Your friend has n cards.

You know that each card has a lowercase English letter on one side and a digit on the other.

Currently, your friend has laid out the cards on a table so only one side of each card is visible.

You would like to know if the following statement is true for cards that your friend owns: "If a card has a vowel on one side, then it has an even digit on the other side." 
More specifically, a vowel is one of 'a', 'e', 'i', 'o' or 'u', and even digit is one of '0', '2', '4', '6' or '8'.

For example, if a card has 'a' on one side, and '6' on the other side, then this statement is true for it. 
Also, the statement is true, for example, for a card with 'b' and '4', and for a card with 'b' and '3' (since the letter is not a vowel). The statement is false, for example, for card with 'e' and '5'. 
You are interested if the statement is true for all cards. In particular, if no card has a vowel, the statement is true.

To determine this, you can flip over some cards to reveal the other side. 
You would like to know what is the minimum number of cards you need to flip in the worst case in order to verify that the statement is true.

Input
The first and only line of input will contain a string s (1 ≤ |s| ≤ 50), denoting the sides of the cards that you can see on the table currently. 
Each character of s is either a lowercase English letter or a digit.

Output
Print a single integer, the minimum number of cards you must turn over to verify your claim.

Input:
ee

Output:
2
"""
s = input()
vowels = "aeiou" 
ans = 0
for c in s:
    if(c in vowels):
        ans += 1
    elif(c.isnumeric()):
        num = int(c)
        if(num % 2 == 1):
            ans += 1
            
print(ans)