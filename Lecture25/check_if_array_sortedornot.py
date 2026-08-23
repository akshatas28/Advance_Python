# advanced python

# lect 25 : check if arr is sorted or not

# simple

# using sorting

num=[3,5,6,8,9,10,20]
nums1 = num[:]
nums1.sort()
if num==nums1:
    print("array is sorted")
else:
    print("array is not sorted")
    

# else

num=[3,5,6,8,9,10,20]
count=0
for i in range(len(num)-1):
    if num[i]<=num[i+1]:
        count+=1
    else:
        print("array is not sorted")
        break
if count==len(num)-1:
    print("array is sorted")

# recursion

num=[3,5,6,8,9,10,20]

def sortarr(num, i , count):
    if i==len(num)-1:
        return True
    if count==len(num)-1:
        return True
    if len(num)<=1:
        return True
    if num[i]<num[i+1]:
        return sortarr(num, i+1 , count+1)
    return False
        
print(sortarr(num, 0 , 0))