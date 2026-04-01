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
CMPUT 331 Assignment 9 Problem 3 Student Solution 
March 2026 
Author: <Your name here>
"""


from sys import flags
from typing import List


SYMBOLS = "AEIOGNLTSR"


def getCubeRoot(value: int) -> int:
    "Return the integer cube root of a perfect cube."
    if value < 0:
        raise ValueError("Negative value is not a perfect cube.")
    

    low = 0
    high = value

    while low <= high:
        #get mid which is the average of low and high
        mid = (low + high) // 2
        #get the cube of mid
        cube = mid * mid * mid
        if cube == value:
            return mid
        if cube < value:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("Ciphertext block is not a perfect cube.")


def decodeBlock(block: int, block_size: int) -> str:
    "Decode one plaintext block integer into block_size symbols."
    

    base = len(SYMBOLS)
    message = []
    for _ in range(block_size):
        message.append(SYMBOLS[block % base])
        block //= base
    return ''.join(message)


def NSizeHack(blocks: List[int], n: int) -> str:
    """
    Hack RSA knowing block size is 6, e is 3, and that none of the words end in the letter A 
    """
    #idea is that encryption is c = m^3 mod n,
    #so that decryption is m = c^1/3 mod n
    #if m ^ 3 < n then technically the mod n part doesnt do anything
    #so c = m^3 and so m = c^1/3 
    #so for each ciphertext block i need to take the integre cube root
    #then use that to decode that integer back into text

    plaintext = ""

    for block in blocks:
        #get the integer cube root of the block
        m = getCubeRoot(block)

        #decode the block using 6 symbols
        blockText = decodeBlock(m, 6)

        #add it to the plaintext
        plaintext += blockText
        
    return plaintext.rstrip('A')


def test():
    "Run tests"
    n = 14118956157108293655346808051133433894091646039538312006923399735362493605263203702497585893776717003286326229134304078204210728995962809448233282087726441833718356477474042405336332872075207334696535304102256981804931805888502587515310873257966538377740407422137907772437613376342940374815839154897315760145075243071401233858428232725214391295151698044147558454184807105787419519119343953276836694146614061330872356766933442169358208953710231872729486994792595105820069351163066330362191163434473421951082966346860965671789280887020440983279967498480147232734401682910892741619433374703999689201536556462802829353073
    blocks = [140932729664]
    assert NSizeHack(blocks, n) == "GAIN"
    blocks = [2744000]
    assert NSizeHack(blocks, n) == "AGE"
    blocks = [80286111144000, 2744]
    assert NSizeHack(blocks, n) == "AGEOGAGE"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


if __name__ == '__main__' and not flags.interactive:
    test()
