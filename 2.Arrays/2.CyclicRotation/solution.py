# If we want our solution to be scalable, we need to omit the rotations that
# are useless. For instance:
# A = [1, 2, 3, 4]
# K = 4
# the function should return [1, 2, 3, 4]
# But we also have
# A = [1, 2, 3, 4]
# K = 8
# the function should return [1, 2, 3, 4]
# The pattern is that if K is a multiple of the length of A, the output is A
# If K is not a multiple of the length of A, we need to rotate indices.
# But to omit the useless rotations, let's take K modulo len_A
def solution(A, K):
    # Let's store the length of A:
    len_A = len(A)
    # if A is empty, let's return A:
    if len_A == 0:
        return A
    # K modulo len_A:
    K_net = K % len_A
    if K_net > 0:
        # Moving elements from the right to left:
        head = A[len_A - K_net:]
        # Moving elements from the left to rigth:
        tail = A[:-K_net]
        # Let's recompose the final answer:
        return head + tail
    else:
        return A
