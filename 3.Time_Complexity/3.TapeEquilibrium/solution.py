# A =[3, 1, 2, 4, 3]
# For this one, it is important to re-use previous calculations. For instance:
# (A[0] + A[1] + A[2]) = (A[0] + A[1]) + A[2]
def solution(A):
    #
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    # Important not to include the first and last element
    for index in range(1, len(A)-1):
        # Increment tail and head
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif
