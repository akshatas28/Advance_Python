# advanced python

# lect 18 : selection sort : prefer nested loops / iterative approach

num = [ 5, 7, 8, 4,1,6,9,2 ]
def selectionsort():
    for i in range(len(num)):
        minindex= i
        for j in range(i+1, len(num)):
            if num[j]<num[minindex]:
                minindex=j
        num[i], num[minindex] = num[minindex] , num[i]
    return (num)

print(selectionsort())


# recursion

def slctsort (num, i, j):
    if i==len(num):
        return (num)
    minindex = i
    if j<len(num):
        if num[j]<num[minindex]:
            minindex=j
            num[i], num[minindex] = num[minindex] , num[i]
            return slctsort(num, i , j+1)
        else:
            return slctsort(num, i , j+1)
    return slctsort(num, i+1 , i+2)
        

i=0
print(slctsort([ 5, 7, 8, 4,1,6,9,2 ], i, i+1))

# alternative : much efficient

def selection_sort_recursive(num, i=None, j=None, min_idx=None):
    if i is None or j is None or min_idx is None:
        i = 0
        j = 1
        min_idx=0
    # Base Case 1: Outer loop finish (entire list sorted)
    if i == len(num):
        return num
        
    # Base Case 2: Inner loop finish (j reached the end of the list)
    if j == len(num):
        # Swap the starting element with the absolute minimum found
        num[i], num[min_idx] = num[min_idx], num[i]
        # Move to the next outer element (i+1), reset j and min_idx
        return selection_sort_recursive(num, i + 1, i + 2, i + 1)

    # Core Logic: Accessing elements to update the minimum index tracker
    if num[j] < num[min_idx]:
        min_idx = j  # Found a smaller number, update tracking index

    # Move to the next element in the inner scan (j+1)
    # Crucial: Pass the updated min_idx forward so it doesn't reset!
    return selection_sort_recursive(num, i, j + 1, min_idx)

# Execution
my_list = [5, 7, 8, 4, 1, 6, 9, 2]
print(selection_sort_recursive(my_list))
# Output: [1, 2, 4, 5, 6, 7, 8, 9]