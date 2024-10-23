from math import gcd


def solution(lst):
    return gcd(*lst) * len(lst)
