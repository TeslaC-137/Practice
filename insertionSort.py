def insertionSort(A):
    for i in range(1, len(A)):
        j = i-1
        while j>=0 and A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1

            
