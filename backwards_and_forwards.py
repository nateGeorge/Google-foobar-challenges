'''
Backward and forward
====================

The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, has a revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!" 

To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b, at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4
'''

def baseN(num, b):
    basePoss = "0123456789abcdefghijklmnopqrstuvwxyz"
    return ((num == 0) and basePoss[0]) or (baseN(num // b, b).lstrip(basePoss[0]) + basePoss[num % b])

def answer(n):
    palindrome = False
    cnt = 2
    while not palindrome:
        test = baseN(n, cnt)
        if test == test[::-1]:
            palindrome = True
        else:
            cnt+=1
    return cnt

	
if __name__=='__main__':
    print(answer(0))
    print(answer(42))