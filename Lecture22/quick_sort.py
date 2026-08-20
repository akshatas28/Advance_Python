# advanced python

# lect 22 : quick sort : 

# below is only for array partition

num=[ 4,1,7,6,3,2,8 ]

def partition(num, low, high):
    pivot = num[low]
    i = low
    j = high
    while i< j:
        while num[i] <= pivot and i <= high-1:
            i+=1
        while num[j] >= pivot and j >= low+1:
            j-=1
        if i< j:
            num[i] , num[j] = num[j] , num[i]
    num[low], num[j] = num[j] , num[low]
    left_arr = num[:j]
    right_arr = num[j:]
    return (j, left_arr, right_arr)

print(partition(num, 0, len(num)-1))

# below is entire quick sort

# Hoare-Partitioning Quick Sort
num=[ 4,1,7,6,3,2,8 ]

def partition(num, low, high):
    
    if low >= high:
        return num
    pivot = num[low]
    i = low
    j = high
    while i< j:
        while num[i] <= pivot and i <= high-1:
            i+=1
        while num[j] >= pivot and j >= low+1:
            j-=1
        if i< j:
            num[i] , num[j] = num[j] , num[i]
    num[low], num[j] = num[j], num[low]
    partition(num, low, j-1)
    partition(num, j+1, high)
    return num

print(partition(num, 0, len(num)-1))


# merged one

def partition(num, low, high):
    pivot = num[low]
    i = low
    j = high
    while i< j:
        while num[i] <= pivot and i <= high-1:
            i+=1
        while num[j] >= pivot and j >= low+1:
            j-=1
        if i< j:
            num[i] , num[j] = num[j] , num[i]
    num[low], num[j] = num[j] , num[low]
    return j

def quicksort(num, low, high):
    # Base Case: If the window has 0 or 1 elements, it is already sorted!
    if low >= high:
        return
        
    # Get the split point where the pivot ended up
    pivot_index = partition(num, low, high)
    
    # Recursively sort the left chunk (everything before the pivot)
    quicksort(num, low, pivot_index - 1)
    
    # Recursively sort the right chunk (everything after the pivot)
    quicksort(num, pivot_index+1, high)
    
    return num

# Running it:
my_list = [4, 1, 7, 6, 3, 2, 8]
print(quicksort(my_list, 0, len(my_list)-1))

# when pivot is mid

def quicksort_clean(num, low, high):
    if low >= high:
        return num
        
    # 1. Pick a middle pivot value (safely stored as a VALUE, not a moving index!)
    pivot_value = num[(low + high) // 2]
    i, j = low, high
    
    # 2. Let simple local while loops handle the pointer movement
    while i <= j:
        while num[i] < pivot_value: i += 1
        while num[j] > pivot_value: j -= 1
        
        if i <= j:
            num[i], num[j] = num[j], num[i]  # Swap out-of-place elements
            i += 1
            j -= 1
            
    # 3. Once pointers cross, recursively sort the split left and right zones
    quicksort_clean(num, low, j)
    quicksort_clean(num, i, high)
    
    return num

num=[ 4,1,7,6,3,2,8 ]
print(quicksort_clean(num, 0, len(num)-1))