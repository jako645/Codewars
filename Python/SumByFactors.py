from math import sqrt
from itertools import chain


def get_prime_factors(num):
    num = abs(num)
    result = []

    while num % 2 == 0:
        result.append(2)
        num = num // 2

    for potential_factor in range(3, int(sqrt(num)) + 1, 2):
        while num % potential_factor == 0:
            result.append(potential_factor)
            num = num // potential_factor

    if num > 2:
        result.append(num)

    return result


def delete_duplicates(lst):
    return list(set(lst))


def sum_for_list(lst):
    prime_factors = map(get_prime_factors, lst)
    prime_factors = list(chain.from_iterable(prime_factors))
    prime_factors = delete_duplicates(prime_factors)
    prime_factors = sorted(prime_factors)

    result = []
    for factor in prime_factors:
        sum_ = sum(number for number in lst
                   if number % factor == 0)
        result.append([factor, sum_])

    return result
