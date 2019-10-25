A = [1, 3, 1, 4, 2, 3, 5, 4]

def solution(X, A):
    l_current = set()
    l_needed = set(range(1,X+1))
    time = -1 #initialization
    for k_index, k_value in enumerate(A):
        l_current.add(k_value)
        #print(l_current)
        if l_current == l_needed:
            time = k_index
            break
    return time
