# In this problem, we need to find the binary gap within a positive integer N.
# That is, any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
# Example 1: number 9 has binary representation 1001 and contains a binary gap of length 2.
# Example 2: 32 has binary representation '100000' and thus no binary gaps.
import re

def solution(A):
    # Let's first find the binary represent of N using the function bin
    # The function bin() gives a binary string, prefixed with 0b
    # Let's ignore 0b:
    binary_number = bin(A)[2:]
    # Let's use the special character '+':
    # '+' Causes the resulting RE to match 1 or more repetitions of the preceding RE
    # source: https://docs.python.org/2.6/library/re.html
    zeros = re.findall(r'0+', binary_number)
    # If first element is not 1, ignore the first sequence of zeroes extracted
    if binary_number[0] != '1':
        zeros = zeros[1:]
    # If last element is not a one, ignore the last sequence of zeroes extracted
    if binary_number[-1] != '1':
        zeros = zeros[:-1:]
    # If the string contains no zeroes, there is no binary gap
    if not zeros:
        return 0
    return len(max(zeros))
