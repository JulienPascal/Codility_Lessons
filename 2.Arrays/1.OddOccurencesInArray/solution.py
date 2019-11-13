# The goal is to find an unrepeated element in the array A.
# We also want the solution to be efficient.
# A super efficient solution is to use the XOR operator.
# Because b XOR b = 0 and 0 XOR a = a, by applying the XOR operator repetitively
# repeated elements are cancelled, and we are left with the only non-repeated
# element.
def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result
