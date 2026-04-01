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
CMPUT 331 Assignment 9 Problem 4 Student Solution 
March 2026 
Author: <Your name here>
"""


from math import isqrt
from sys import flags


def isPerfectSquare(value: int) -> bool:
    "Return True when value is a perfect square."
    if value < 0:
        return False
    root = isqrt(value)
    return root * root == value

def fermat(n: int):
    a  = isqrt(n)
    if a * a < n:
        a += 1
   
    #Citation: https://en.wikipedia.org/wiki/Fermat%27s_factorization_method 
    #refer to readme for more details on how this works
    while True:
        b2 = a * a - n
        if isPerfectSquare(b2):
            b = isqrt(b2)
            p = a - b
            q = a + b
            return p, q
        a += 1

def neighboringPrimesHack(n: int, e: int) -> int:
    """
    Hack RSA assuming the primes used to generate n are neighboring primes
   """
    p, q = fermat(n)
    phi = (p - 1) * (q - 1)
    #compute the modular inverse of e mod phi to get d
    d = pow(e, -1, phi)
    return d 


def test():
    "Run tests"
    n = 2258724439526021544157047621119350583197447599193184675599358763050848257586056828104876705650962354020284656819514092184827108564186652876034812304096925234526529102930003243145695407270292310072497277305040214326910606519683485744152752287098279548538437871821282499190097069731978324838562972431848673202153997392532099768480138378599593632338015547570401669892770035801762510991016962174366002521569162275345168719593756357806872004536221802593156449508264546662919124522041123146692980555122158986154353971683728243502201158326571121734904418229587768180587564060634571714388931274357530244543544695318021344901
    e = 65537
    assert neighboringPrimesHack(n, e) == 1024847489719483293972167906092817934021381842464692303792095033005478184652623492691557650170697721274199071595969773489906753441028034696763220450655754288018689738693052419826668883693019395643922960128517872548713151280487482370082949204405975870963562393098214083585100423662207721857874308378983660319154444021508123623874335581975952113458400019718945782474434821002356689048723284246890292809975008327297155457612436552844514897316197222905685306128814161516680035297345653640064009770162031566796977683846478544923575404448902250286550221966045366790038028309208157137672722514680364349046053361402392834049
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


if __name__ == '__main__' and not flags.interactive:
    test()
