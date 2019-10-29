# Is A a permutation?
# A is composed on integers. There should be no "gaps"
# between integers. I use the operator XOR.
# It works because XOR is both associative and its self inverse.
# Example with A = [1, 2], which is a permutation.
# test = A[0] ^ 1 ^ A[1] ^ 2
# = 1 ^ 1 ^ 2 ^ 2
# = 0 ^ 0
# = 0
# When the value of test is 0, A is a permutation.
# test with A = [1, 3], which is not a permutation.
def solution(A):
    if len(A)==0:
        raise("A is empty")
    test = A[0] ^ 1
    for i, a in enumerate(A[1:], start=2):
        test ^= a ^ i
    if test==0:
        output = 1
    else:
        output = 0
    return output
