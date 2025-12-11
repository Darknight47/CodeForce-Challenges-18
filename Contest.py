"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/551/A --------------------------------------------

Professor GukiZ likes programming contests. He especially likes to rate his students on the contests he prepares. 
Now, he has decided to prepare a new contest.

In total, n students will attend, and before the start, every one of them has some positive integer rating. Students are indexed from 1 to n. 
Let's denote the rating of i-th student as ai. After the contest ends, every student will end up with some positive integer position. GukiZ expects that his students will take places according to their ratings.

He thinks that each student will take place equal to . 
In particular, if student A has rating strictly lower then student B, A will get the strictly better position than B, and if two students have equal ratings, they will share the same position.

GukiZ would like you to reconstruct the results by following his expectations. Help him and determine the position after the end of the contest for each of his students if everything goes as expected.

Input
The first line contains integer n (1 ≤ n ≤ 2000), number of GukiZ's students.

The second line contains n numbers a1, a2, ... an (1 ≤ ai ≤ 2000) where ai is the rating of i-th student (1 ≤ i ≤ n).

Output
In a single line, print the position after the end of the contest for each of n students in the same order as they appear in the input.

Input:
3
1 3 3

Output.
3 1 1
"""
sze = int(input())
arr = list(map(int, input().split()))
arrCopy = sorted(arr.copy())

positions_map = {}

for i, num in enumerate(arrCopy):
    # overwrite so we store the LAST occurrence index
    positions_map[num] = i
for num in arr:
    pos = sze - positions_map[num]
    print(pos, end=" ")
# positions = []
# for num in arr:
#     numIdx = arrCopy.index(num) + 1
#     pos = 1
#     for n in range(numIdx, sze):
#         if(arrCopy[n] > num):
#             pos += 1
#     positions.append(pos)
# print(*positions)