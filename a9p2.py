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
CMPUT 331 Assignment 9 Problem 2 Student Solution 
March 2026 
Author: Precious Ajilore
"""


from sys import flags
from typing import List


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def blockSizeHack(blocks: List[int], n: int, e: int) -> str:
    """
    Hack RSA assuming a block size of 1
    """
    #for every symbol in SYMBOLS, get its index 
    # then i have to encrypt that index with RSA using pow(index, e, n) where
    # e is the public exponent and n is the modulus and the index is the plaintext
    # store the result in a dictionary where the key is the encrypted block and the value
    # is the original symbol

    #print(blocks)

    lookup ={}

    for index, symbol in enumerate(SYMBOLS):
        #encrypt the index using RSA
        encrypted_block = pow(index, e, n)
        #print(f"Symbol: {symbol}, Index: {index}, Encrypted Block: {encrypted_block}")

        #store the mapping from the encrypted block to the original symbol
        lookup[encrypted_block] = symbol
    
    
    return ''.join(lookup[block] for block in blocks)


def test():
    "Run tests"
    blocks = [2361958428825, 564784031984, 693733403745, 693733403745,2246930915779, 1969885380643]
    n = 3328101456763
    e = 1827871
    assert blockSizeHack(blocks, n, e) == "Hello."
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


if __name__ == '__main__' and not flags.interactive:
    test()
