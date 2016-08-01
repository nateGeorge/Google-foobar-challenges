'''
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight, and so on. Each string is one of: 

"L" : put weight on left-hand side 
"R" : put weight on right-hand side 
"-" : do not use weight 

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 2
Output:
    (string list) ["L", "R"]

Inputs:
    (int) x = 8
Output:
    (string list) ["L", "-", "R"]

I manually went through and looked at some cases for a pattern:
0 []
1 [r]
2 [l,r]
3 [-,r]
4 [r,r]
5 [l,l,r]
6 [-,l,r]
7 [r,l,r] for second label, 9-7 > 4-3: L
8 [l,-,r] for second label, 9-8 > 4-3:  ls - rs > sum-series: L; rs-ls>sum-series: R
9 [-,-,r]
10[r,-,r]
11[l,r,r] for second label, 11-9 > 4-3: R
12[-,r,r]
13[r,r,r]
14[l,l,l,r]
15[-,l,l,r]
16[r,l,l,r]
17[l,-,l,r]
18[-,-,l,r]
19[r,-,l,r]
20[l,r,l,r]
21[-,r,l,r]
22[r,r,l,r]
23[l,l,-,r]
24[-,l,-,r]
25[r,l,-,r]
26[l,-,-,r]
27[-,-,-,r]
28[r,-,-,r]
29[l,r,-,r]

The rightmost column is always r.  After that, if the right-left>sum-series at that index, assign 'l', if left-right>sum-series, assign 'r'.

'''

from itertools import takewhile, count
def answer(x):
    if (x == 0):
        return []
    i = takewhile(lambda y: y/3<x, (sum([3**(q) for q in range(j)]) for j in count(1)))
    sums = list(i)
    length = len(sums)
    ans = ['-']*length
    
    series = [3**j for j in range(length)]
    rs = series.pop()
    ls = x
    ans[-1] = 'R'
    
    while len(series) > 0:
        nextS = series.pop()
        if rs-ls > sums[len(series)] - nextS:
            ans[len(series)] = 'L'
            ls += nextS
        elif ls - rs > sums[len(series)] - nextS:
            ans[len(series)] = 'R'
            rs += nextS
    
    return ans