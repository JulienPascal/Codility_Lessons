# A = [1, 3, 1, 4, 2, 3, 5, 4]
# I am using Python sets module. The set l_current stores the leaves already in
# place at time k. The set l_needed is the minimal set of leaves needed to cross
# the river. When the two set are equal, it's time to cross the river
def solution(X, A):
    l_current = set()
    l_needed = set(range(1,X+1))
    time = -1 #initialization
    for k_index, k_value in enumerate(A):
        l_current.add(k_value)
        if l_current == l_needed:
            time = k_index
            break
    return time
