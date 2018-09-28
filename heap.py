
# This function corrects ONE VIOLATION of heap
def max_heapify(A, i, heapsize):
    # if a node is a leaf node
    if 2*i+1 > heapsize-1:
        return
    # if a node has two children
    if 2*i+2 <= heapsize-1:
        if A[2*i+1] > A[2*i+2]:
            Max = 2*i+1
        else:
            Max = 2*i+2
    # if a node has only one child
    else:
        Max = 2*i+1
    # if heap property is violated
    if A[Max] > A[i]:
        A[Max], A[i] = A[i], A[Max]
        #once we swap elements there is chance that heap property is violated in swapped position
        #so to correct that we call heapify again in swapped position
        max_heapify(A, Max, heapsize)
"""Time complexity is O(log n) """

# turns a list into a max heap
def heapify(A, heapsize):
    """In a complete binary tree, which a heap is, of size n, there are n//2 inner nodes,
    Since leaves are already a heap, we only call heapify in inner nodes.
    We go up from down to maitain precondition of max_heapify, that is there is only one
    violaiton of heap"""
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i, heapsize)
    return A
"""In simple analysis time complexity seems to be O(nlog n). But careful analysis
shows it is actually O(n)
At each level we have to do work proportional to height of heap, that is level of
heap below it, since there are exponentially less nodes as we go up actual amount of
work that has to be done is very less than nlog n. Eg, there is only one node, root node,
where log n work is to be done, level below will have to to log(n/2) work and level
below it will have to do log(n/4) work and so on"""

def heapsortSlow(A):
    heapsize = len(A)
    for i in range(len(A)-2):
        heapify(A, heapsize)
        A[0], A[heapsize-1] = A[heapsize-1], A[0]
        heapsize -= 1

"""This takes O(n^2 time) """
def heapsort(A):
    heapify(A, len(A))
    A[0], A[len(A)-1] = A[len(A)-1], A[0]
    heapsize = len(A)-1
    for i in range(heapsize-2):
        max_heapify(A, 0, heapsize)
        A[0], A[heapsize-1] = A[heapsize-1], A[0]
        heapsize -= 1
    

