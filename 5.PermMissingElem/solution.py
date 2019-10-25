# Wrong one
A = [2, 3, 1, 5]
A = [1, 2, 3]
def solution(A):
    # Initialize output.
    # Value of 0 is a flag for the fact that there are
    # no missing elements in A
    output = 1
    if len(A)!=0:
        A_min=1
        A_max=max(A)
        # Construct list of integers, including the missing element
        l = list(range(A_min, A_max+1))
        # Take the set difference:
        missing = list(set(l) - set(A))
        if len(missing) != 0:
            output = int(missing[0])
    return output



This problem has a mathematical solution, based on the fact that the sum of consecutive integers from 1 to n is equal to n(n+1)/2.
Using this formula we can calculate the sum from 1 to N+1. Then with O(N) time complexity we calculate the actual sum of all elements in the array.
The difference between the full and actual totals will yield the value of the missing element.
Space complexity is O(1).

def solution(A):
    # Initialize output.
    # Value of 0 is a flag for the fact that there are
    # no missing elements in A
    output = 1
    if len(A)!=0:
        A_min=1
        A_max=max(A)
        sum_1 = (A_max+1)*A_max/2
        # Take the set difference:
        sum_2 = sum(A)
        output=int(sum_1 - sum_2)
    return output

def solution(A):
    # write your code in Python 2.7
    sum = 0
    N = len(A)
    for val in A:
        sum += val

    expected = (N + 1) * (N + 2) // 2;

    return expected - sum
