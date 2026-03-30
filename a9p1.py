#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Insert your name here>>
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
Author: <Your name here>
"""


from math import isqrt
from sys import flags
from typing import List, Tuple


def _primes_up_to(limit: int) -> List[int]:
    "Return all primes <= limit using a sieve."
    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (((limit - start) // candidate) + 1)

    return [value for value in range(2, limit + 1) if sieve[value]]


def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    for p in _primes_up_to(min(t, isqrt(n))):
        if n % p != 0:
            continue

        q = n // p
        if q > t:
            continue

        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        return (p, q, d)

    raise ValueError("No valid prime factors found within the threshold.")


def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == (17, 29, 269)
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking



if __name__ == '__main__' and not flags.interactive:
    test()
