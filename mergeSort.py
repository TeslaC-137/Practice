def merge(A, B):
    i, j = 0, 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        elif B[j] < A[i]:
            result.append(B[j])
            j += 1
        else:
            result.append(A[i])
            result.append(B[j])
            i += 1
            j += 1
    if i >= len(A):
        result.extend(B[j:])
    else:
        result.extend(A[i:])
    return result

def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

    
            
