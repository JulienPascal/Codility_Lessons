# This problem has a quite nice solution.
# The sum of the first N integers is N*(N+1)/2.
# We can calculate the actual sum of elements in A.
# The difference between the expected sum and the actual one is the number
# we are looking for.
def solution(A):
    # write your code in Python 2.7
    sum = 0
    N = len(A)
    for val in A:
        sum += val
    expected = (N + 1) * (N + 2) // 2;
    return expected - sum
