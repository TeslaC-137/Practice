def findKth(A, B, k):
    if len(A) > k:
        astart = len(A) - k
    else:
        astart = 0
    if len(B) > k:
        bstart = len(B)-k
    else:
        bstart = 0
    aend, bend = len(A)-1, len(B)-1
    kth = getKth(A, B, astart, bstart, aend, bend, k)
    return kth

def getKth(A, B, astart, bstart, aend, bend, k):
    if astart > aend:
        return B[bend-k+1]
    if bstart > bend:
        return A[aend-k+1]
    if astart == aend and bstart == bend:
        if k == 1:
            return max(A[astart], B[bstart])
        if k == 2:
            return min(A[astart], B[bstart])
    amid = (astart+aend)//2
    bmid = (bstart+bend)//2
    if A[amid] < B[bmid]:
        return getKth(A, B, amid+1, bstart, aend, bmid, k-bend+bmid)
    else:
        return getKth(A, B, astart, bmid+1, amid, bend, k - aend+amid)
    

