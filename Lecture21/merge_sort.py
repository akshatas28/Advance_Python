# advanced python

# lect 21 : merge sort : 

leftarr=[1,2,3,4]
rightarr=[1,1,3,4,5,6,7]
def merge2arrs():
    p1 = 0
    p2 = 0
    i =0
    mergedarr = [0]*(len(leftarr)+len(rightarr))
    while ((p1 < len(leftarr)) and (p2 < len(rightarr))):
        if leftarr[p1] < rightarr[p2]:
            mergedarr[i]+= leftarr[p1]
            i+=1
            p1+=1
        elif leftarr[p1] == rightarr[p2]:
            mergedarr[i] += leftarr[p1]
            i+=1
            p1+=1
            mergedarr[i] += rightarr[p2]
            i+=1
            p2+=1
        else:
            mergedarr[i] += rightarr[p2]
            i+=1
            p2+=1
    while p1 < len(leftarr):
        mergedarr[i] = leftarr[p1]
        i += 1
        p1 += 1
    while p2 < len(rightarr):
        mergedarr[i] = rightarr[p2]
        i += 1
        p2 += 1
    return mergedarr

print(merge2arrs())

# below is also a code possibility, but the TC increaes by sqare

leftarr=[1,2,3,4]
rightarr=[1,1,3,4,5,6,7]
def merge2arrs():
    leftarr=[1,2,3,4]
    rightarr=[1,1,3,4,5,6,7]
    i =0
    mergedarr = [0]*(len(leftarr)+len(rightarr))
    while (leftarr!=[]) and ( rightarr!=[]):
        if leftarr[0] < rightarr[0]:
            mergedarr[i]+= leftarr[0]
            i+=1
            leftarr=leftarr[1:]
        elif leftarr[0] == rightarr[0]:
            mergedarr[i]+=leftarr[0]
            i+=1
            mergedarr[i]+= rightarr[0]
            i+=1
            leftarr=leftarr[1:]
            rightarr=rightarr[1:]
        else:
            mergedarr[i] += rightarr[0]
            i+=1
            rightarr=rightarr[1:]
    else:
        if rightarr==[]:
            mergedarr[i:] = leftarr
            leftarr=leftarr[0:]
        if leftarr==[]:
            mergedarr[i:] = rightarr
            rightarr=rightarr[0:]
    return mergedarr

print(merge2arrs())

# recursion

def mergerecursion(leftarr, rightarr, mergedarr, i):
    if leftarr==[]:
        mergedarr[i:] = rightarr
        return mergedarr
    if rightarr==[]:
        mergedarr[i:] = leftarr
        return mergedarr
    if (leftarr!=[]) and (rightarr!=[]):
        if leftarr[0] < rightarr[0]:
            mergedarr[i] = leftarr[0]
            return mergerecursion(leftarr[1:], rightarr, mergedarr, i+1)
        elif leftarr[0] == rightarr[0]:
            mergedarr[i] = leftarr[0]
            mergedarr[i+1] = rightarr[0]
            return mergerecursion(leftarr[1:], rightarr[1:], mergedarr, i+2)
        else:
            mergedarr[i] = rightarr[0]
            return mergerecursion(leftarr, rightarr[1:], mergedarr, i+1)

leftarr=[1,2,3,4]
rightarr=[1,1,3,4,5,6,7]
mergedarr = [0]*(len(leftarr)+len(rightarr))
print(mergerecursion(leftarr, rightarr, mergedarr, 0))

# below merged code : for merge sort

def mergerecursion(leftarr, rightarr, mergedarr, i):
    if leftarr==[]:
        mergedarr[i:] = rightarr
        return mergedarr
    if rightarr==[]:
        mergedarr[i:] = leftarr
        return mergedarr
    if (leftarr!=[]) and (rightarr!=[]):
        if leftarr[0] < rightarr[0]:
            mergedarr[i] = leftarr[0]
            return mergerecursion(leftarr[1:], rightarr, mergedarr, i+1)
        elif leftarr[0] == rightarr[0]:
            mergedarr[i] = leftarr[0]
            mergedarr[i+1] = rightarr[0]
            return mergerecursion(leftarr[1:], rightarr[1:], mergedarr, i+2)
        else:
            mergedarr[i] = rightarr[0]
            return mergerecursion(leftarr, rightarr[1:], mergedarr, i+1)

def mergesort(num):
    if len(num)<=1:
        return num
    mid = len(num) // 2
    left_half = num[:mid]
    right_half = num[mid:]
    leftarr = mergesort(left_half)
    rightarr = mergesort(right_half)
    mergedarr = [0]*(len(leftarr)+len(rightarr))
    return mergerecursion(leftarr, rightarr, mergedarr, 0)


print (mergesort([ 5, 7, 8, 4,1,6,9,2 ]))