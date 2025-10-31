"""

---------------------------------- Link for the challenge: https://codeforces.com/contest/747/problem/B -----------------------------------

The process of mammoth's genome decoding in Berland comes to its end!

One of the few remaining tasks is to restore unrecognized nucleotides in a found chain s. Each nucleotide is coded with a capital letter of English alphabet: 'A', 'C', 'G' or 'T'. 
Unrecognized nucleotides are coded by a question mark '?'. Thus, s is a string consisting of letters 'A', 'C', 'G', 'T' and characters '?'.

It is known that the number of nucleotides of each of the four types in the decoded genome of mammoth in Berland should be equal.

Your task is to decode the genome and replace each unrecognized nucleotide with one of the four types so that the number of nucleotides of each of the four types becomes equal.

Input
The first line contains the integer n (4 ≤ n ≤ 255) — the length of the genome.

The second line contains the string s of length n — the coded genome. It consists of characters 'A', 'C', 'G', 'T' and '?'.

Output
If it is possible to decode the genome, print it. If there are multiple answer, print any of them. If it is not possible, print three equals signs in a row: "===" (without quotes).

Input:
8
AG?C??CT

Output:
AGACGTCT
"""
from collections import Counter

sze = int(input())
genome = list(input())

if sze % 4 != 0:
    print("===")
else:
    counts = Counter(genome)
    a = counts['A']
    c = counts['C']
    g = counts['G']
    t = counts['T']
    q = counts['?']

    target = sze // 4

    aa = target - a
    cc = target - c
    gg = target - g
    tt = target - t

    # If any already exceeds target, impossible
    if aa < 0 or cc < 0 or gg < 0 or tt < 0:
        print("===")
    # If total needed doesn’t match number of '?', impossible
    elif aa + cc + gg + tt != q:
        print("===")
    else:
        for i in range(sze):
            if genome[i] == '?':
                if aa > 0:
                    genome[i] = 'A'
                    aa -= 1
                elif cc > 0:
                    genome[i] = 'C'
                    cc -= 1
                elif gg > 0:
                    genome[i] = 'G'
                    gg -= 1
                elif tt > 0:
                    genome[i] = 'T'
                    tt -= 1
        print("".join(genome))