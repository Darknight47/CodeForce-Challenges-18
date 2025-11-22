"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/919/A -----------------------------------------

We often go to supermarkets to buy some fruits or vegetables, and on the tag there prints the price for a kilo. 
But in some supermarkets, when asked how much the items are, the clerk will say that a yuan for b kilos (You don't need to care about what "yuan" is), the same as a/b yuan for a kilo.

Now imagine you'd like to buy m kilos of apples. You've asked n supermarkets and got the prices. Find the minimum cost for those apples.

You can assume that there are enough apples in all supermarkets.

Input
The first line contains two positive integers n and m (1 ≤ n ≤ 5000, 1 ≤ m ≤ 100), denoting that there are n supermarkets and you want to buy m kilos of apples.

The following n lines describe the information of the supermarkets. Each line contains two positive integers a,b (1 ≤ a, b ≤ 100), 
denoting that in this supermarket, you are supposed to pay a yuan for b kilos of apples.

Output
The only line, denoting the minimum cost for m kilos of apples. Please make sure that the absolute or relative error between your answer and the correct answer won't exceed 10^−6.

Formally, let your answer be x, and the jury's answer be y. Your answer is considered correct if |x−y|max(1,|y|)≤10−6.

Input:
3 5
1 2
3 4
1 3

Output:
1.66666667
"""
n, m = map(int, input().split())
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    price_per_kilo = a / b
    tempPrice = m * price_per_kilo
    ans.append(tempPrice)
ans.sort()
print(ans[0])
