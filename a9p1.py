#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Precious Ajilore
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
CMPUT 331 Assignment 9 Problem 1 Student Solution 
March 2026 
Author: Precious Ajilore
"""


from sys import flags
from typing import Tuple, List
from math import isqrt

def primeSieve(n: int) -> List[int]:
    """
    Return a list of all primes up to n using the Sieve of Eratosthenes
    """
    if n < 2:
        return []
    
    #create a sieve of size n+1, initialize all to True except for 0 and 1
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    #mark all multiples of each prime as False
    for i in range(2, isqrt(n) + 1):
        #if i is prime, mark all multiples of i as False
        if sieve[i]:
            #mark all multiples of i as False starting from i*i
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    
    if there are no primes larger than t, then i just have to test the primes
    up to t until one divides n and then onced i find p and q, RSA is then easier to compute
    using phi(n) = (p-1)(q-1) and then finding d such that d*e = 1 mod phi(n) or d = e^-1 mod phi(n)

    p or q like at least one had to ve <= sqrt(n)
    return p, q, d
    """
    #generate all the primes up to t, sqrt(n)
    for p in primeSieve(min(t, isqrt(n))):
        #test which one divides n, that is p, 
        if n % p != 0:
            continue
        #once we find p, compute q = n // p
        q = n // p
        if q > t:
            continue
        # compute phi = (p-1)(q-1)
        phi = (p-1) * (q-1)

        #then compute d = e^-1 mod phi(n)
        d = pow(e, -1, phi)
        return (p, q, d)
    
    #return (p,q,d)


def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == (17, 29, 269)
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    assert finitePrimeHack(100, 493, 5) == (17, 29, 269)
    assert finitePrimeHack(2**16, 2604135181, 1451556085) == (48533, 53657, 60765)
    assert finitePrimeHack(50, 221, 5) == (13, 17, 77)



if __name__ == '__main__' and not flags.interactive:
    test()
