"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1537/B ---------------------------------------------------

Riley is a very bad boy, but at the same time, he is a yo-yo master. So, he decided to use his yo-yo skills to annoy his friend Anton.

Anton's room can be represented as a grid with n rows and m columns. Let (i,j) denote the cell in row i and column j. 
Anton is currently standing at position (i,j) in his room. To annoy Anton, Riley decided to throw exactly two yo-yos in cells of the room (they can be in the same cell).

Because Anton doesn't like yo-yos thrown on the floor, he has to pick up both of them and return back to the initial position. 
The distance travelled by Anton is the shortest path that goes through the positions of both yo-yos and returns back to (i,j) by travelling only to adjacent by side cells. 
That is, if he is in cell (x,y) then he can travel to the cells (x+1,y), (x−1,y), (x,y+1) and (x,y−1) in one step (if a cell with those coordinates exists).

Riley is wondering where he should throw these two yo-yos so that the distance travelled by Anton is maximized. But because he is very busy, he asked you to tell him.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then t test cases follow.

The only line of each test case contains four integers n, m, i, j (1 ≤ n, m ≤ 10^9, 1 ≤ i ≤ n, 1 ≤ j ≤ m) — the dimensions of the room, and the cell at which Anton is currently standing.

Output
For each test case, print four integers x1, y1, x2, y2 (1 ≤ x1, x2 ≤ n, 1 ≤ y1 , y2 ≤ m) — the coordinates of where the two yo-yos should be thrown. They will be thrown at coordinates (x1,y1) and (x2,y2).

If there are multiple answers, you may print any.

Input:
7
2 3 1 1
4 4 1 2
3 5 2 2
5 1 2 1
3 1 3 1
1 1 1 1
1000000000 1000000000 1000000000 50

Output:
1 2 2 3
4 1 4 4
3 1 1 5
5 1 1 1
1 1 2 1
1 1 1 1
50 1 1 1000000000
"""
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

cases = int(input())
for _ in range(cases):
    n, m, x, y = map(int, input().split())
    start = (x, y)
    corners = [(1, 1), (1, m), (n, 1), (n, m)]
    bestCost = -1
    bestPairs = None

    for i in range(4):
        for j in range(i + 1, 4):
            A, B = corners[i], corners[j]
            # Picking up the first (closest) yo-yo, then picking up the second one (distance between the two)
            cost = min(manhattan(start, A), manhattan(start, B)) + manhattan(A, B)
            if(cost > bestCost):
                bestCost = cost
                bestPairs = (A, B)
            
    print(bestPairs[0][0], bestPairs[0][1], bestPairs[1][0], bestPairs[1][1])