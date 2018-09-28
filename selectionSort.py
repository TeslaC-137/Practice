"""
Selection Sort: PseudoCode-

for i in range(len(A)-1):
    min = i
    for j in range(i+1, len(A)):
        if A[j] < A[min]:
            min = j
    swap min and i
    
        

"""

def selectionSort(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]

