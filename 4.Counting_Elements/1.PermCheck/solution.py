A = [1, 2]
def solution(A):
    # write your code in Python 3.6
    # Let's use XOR
    if len(A)==0:
        raise("A is empty")
    # XOR element and index
    # Works because XOR is both associative and its self inverse
    test = A[0] ^ 1
    for i, a in enumerate(A[1:], start=2):
        test ^= a ^ i
        # A[0] ^ 1 ^ A[1] ^ 2
        # = 1 ^ 1 ^ 2 ^ 2
        # = 0 ^ 0
    if test==0:
        output = 1
    else:
        output = 0
    return output
