# If the distance to be jumped is a multiple of D, which we check with the
# function modulo (%), then (Y - X) / D gives us the number of jumps needed.
# Otherwise, the number of jumps is (Y - X) / D  (rounded to the closest integer
# from below) plus one extra step.
import math
def solution(X, Y, D):
    jumps = 0
    # If the frog is not already there:
    if X!=Y:
        if (Y - X) % D == 0:
            jumps = (Y - X) / D
        else:
            jumps = math.floor((Y - X) / D) + 1
    return int(jumps)
