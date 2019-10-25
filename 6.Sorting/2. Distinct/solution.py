# For this one, I am Python sets module.
# The set is updated with the function add()
# At the end, I simply convert the set to a list and I take its length
def solution(A):
    # Set of elements in A, which is updated as we move along A
    l_current = set()
    for k_index, k_value in enumerate(A):
        l_current.add(k_value)
    return len(list(l_current))
