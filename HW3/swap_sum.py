def swap_sum(A,B):
    idx_a = 0
    idx_b = 0
    len_a = len(A)
    len_b = len(B)
    
    diff = sum(B) - sum(A) - 10

    while idx_a < len_a and idx_b < len_b:

        if diff / 2  == B[idx_b] -A[idx_a]:
            return (idx_a, idx_b)
        
        elif diff / 2 > B[idx_b] - A[idx_a]:
            idx_b += 1

        else:
            idx_a += 1
    
    return None


