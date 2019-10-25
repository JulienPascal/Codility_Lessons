A =[3, 1, 2, 4, 3]
def solution(A):
    if len(A)==0:
        raise Exception('A is empty')
    ouput = 1 #initialization
    #boundary solutions
    max_left = abs(A[0] - sum(A[1:]))
    max_right = abs(sum(A[0:-1]) - A[-1])
    if max_left<=max_right:
        current_min =  max_left
        current_p = 1
    else:
        current_min =  max_right
        current_p = 2
    for (p_index, p_value) in enumerate(A, start = 0):
        # solution is not valid for the boundaries
        if p_index!=0 and p_index!=len(A)-1:
            potential_min = abs(sum(A[0:p_index]) - sum(A[p_index:]))
            if potential_min<=current_min:
                current_min = potential_min
                current_p = current_p
    return current_p


def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif
