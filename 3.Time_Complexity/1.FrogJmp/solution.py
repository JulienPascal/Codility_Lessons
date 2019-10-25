# Correct, but does not scale well
def solution(X, Y, D):
    # Assumptions on X, Y and D
    # * X, Y and D are integers within the range [1..1,000,000,000];
    # * X ≤ Y.
    jumps = 0
    max_jumps = 1000000000
    # We are already at the final destination
    if X != Y:
        # Brute force: loop
        X_jumps = X
        for x in range(0,max_jumps):
            X_jumps += D
            if X_jumps >= Y:
                jumps = x+1
                break
    return jumps

# Much better solution
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
