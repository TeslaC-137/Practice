"""Sorting a nearly sorted array:

Given an array of nelements, where each element is at most k away from its target position devise an algorithm that sorts in O(nlog k time)"""

#Heapsort works

import heapq
def sortNearlySorted1(A, k):
    heap = []
    #insert first k+1 elements in heap first
    for i in range(k+1):
        heapq.heappush(heap, (A[i], i))
    print(heap)

    for i in range(len(A)):
        # extract min, Min = (minvalue, index of minvalue)
        Min = heapq.heappop(heap)
        print(Min)
        A[i], A[Min[1]] = A[Min[1]], A[i]
        
        print(A)
        # if there is remaining element in list
        if i+k+1 < len(A):
            heapq.heappush(heap, (A[i+k+1], i+k+1))

            
"""Above function keeps A unchanged. This is because index of key stored is static.
When A[i] and A[Min[1]] are switched there is no way to change index of A[i] from i
to Min[1] in heap in less than O(n) time"""

"""Solution is to use O(n) extra space. Copy content of A in sorted order in another
list"""

def sortNearlySorted(A, k):
    heap = []
    for i in range(k+1):
        heapq.heappush(heap, A[i])

    for i in range(len(A)):
        Min = heapq.heappop(heap)
        A[i] = Min
        if i+k+1 < len(A):
            heapq.heappush(heap, A[i+k+1])


        
