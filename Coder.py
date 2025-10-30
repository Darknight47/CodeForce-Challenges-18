"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/384/A --------------------------------------

Iahub likes chess very much. He even invented a new chess piece named Coder. A Coder can move (and attack) one square horizontally or vertically. 
More precisely, if the Coder is located at position (x, y), he can move to (or attack) positions (x + 1, y), (x–1, y), (x, y + 1) and (x, y–1).

Iahub wants to know how many Coders can be placed on an n × n chessboard, so that no Coder attacks any other Coder.

Input
The first line contains an integer n (1 ≤ n ≤ 1000).

Output
On the first line print an integer, the maximum number of Coders that can be placed on the chessboard.

On each of the next n lines print n characters, describing the configuration of the Coders. For an empty cell print an '.', and for a Coder print a 'C'.

If there are multiple correct answers, you can print any.

Input:
2
Output:
2
C.
.C
"""
n = int(input())
oddRow = ''.join('C' if j % 2 == 0 else '.' for j in range(n))
evenRow = ''.join('C' if j % 2 == 1 else '.' for j in range(n))
oddCs = oddRow.count('C')
evenCs = evenRow.count('C')

# Total Cs = number of odd rows * oddCs + number of even rows * evenCs
numOddRows = (n + 1) // 2
numEvenRows = n // 2
cs = numOddRows * oddCs + numEvenRows * evenCs

print(cs)

for i in range(1, n + 1):
    if(i % 2 == 1):
        print(oddRow)
    else:
        print(evenRow)
