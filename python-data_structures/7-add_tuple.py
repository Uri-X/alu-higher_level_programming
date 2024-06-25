#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to have at least 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Take only the first 2 elements of each tuple
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]
    # Compute the sum of corresponding elements
    sum1 = a1 + b1
    sum2 = a2 + b2
    return (sum1, sum2)
