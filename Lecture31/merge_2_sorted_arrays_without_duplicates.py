# advanced python

# lect 31 : merge 2 sorted arrays without duplicates

# simple : 

#nums1 = [ 1,1,1,2,4,6,7 ]
#nums2 = [ 1,2,3,6,7,8,9,10 ]

#nums1 = [1, 2, 2, 3]
#nums2 = [2, 2, 4]

#nums1 = [5, 6, 7]
#nums2 = [1, 2]

#nums1 = [5, 6, 7]
#nums2 = [1, 1, 2]

#nums1 = [1, 2]
#nums2 = [1, 2, 3, 3]

#nums1 = [1, 2]
#nums2 = [1, 2, 3, 4, 5]

#nums1 = [5, 6, 7]
#nums2 = [1, 1, 2]

nums1 = [3, 5, 6]
nums2 = [1, 2, 2, 4]

nums = []

i=0
j=0
while i <len(nums1):
    if j<len(nums2):
        if nums1[i]<nums2[j]:
            if nums1[i] in nums:
                i+=1
            else:
                nums.append(nums1[i])
                i+=1
        elif nums1[i]==nums2[j]:
            if nums1[i] in nums:
                i+=1
                j+=1
            else:
                nums.append(nums1[i])
                i+=1
                j+=1
        else:
            if nums2[j] in nums:
                j+=1
            else:
                nums.append(nums2[j])
                j+=1
    else:
        if nums1[i] in nums:
            i+=1
        else:
            nums.append(nums1[i])
            i+=1

while j <len(nums2):
    if nums2[j] in nums:
        j+=1
    else:
        nums.append(nums2[j])
        j+=1

print(nums)


# one can attempt with below

# 1. Initialize completely empty
nums = []
i = 0
j = 0

while i < len(nums1):
    if j < len(nums2):
        if nums1[i] < nums2[j]:
            # 2. Check if empty OR if the new number is larger than the last element
            if not nums or nums1[i] > nums[-1]:
                nums.append(nums1[i])
            i += 1
            
        elif nums1[i] == nums2[j]:
            if not nums or nums1[i] > nums[-1]:
                nums.append(nums1[i])
            i += 1
            j += 1
            
        else:
            if not nums or nums2[j] > nums[-1]:
                nums.append(nums2[j])
            j += 1
    else:
        if not nums or nums1[i] > nums[-1]:
            nums.append(nums1[i])
        i += 1

while j < len(nums2):
    if not nums or nums2[j] > nums[-1]:
        nums.append(nums2[j])
    j += 1

print(nums)