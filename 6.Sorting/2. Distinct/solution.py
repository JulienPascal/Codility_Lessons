def solution(A):
    l_current = set()
    for k_index, k_value in enumerate(A):
        l_current.add(k_value)
    return len(list(l_current))
