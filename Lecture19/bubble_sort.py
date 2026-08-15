# advanced python

# lect 19 : bubble sort : 

# before anything, try playing with loops and thats how i discovered the below code : a prime example of exchange sort

num = [ 5, 7, 8, 4,1,6,9,2 ]
def xyzsort():
    for i in range(len(num)): 
        for j in range(i+1, len(num)):
            if num[j]<num[i]:
                num[i], num[j] = num[j] , num[i]
        
    return (num)

print(xyzsort())

# Time (O(n^2)) always | Space (O(1)) | High memory write overhead.

# classic bubble sort

num = [ 5, 7, 8, 4,1,6,9,2 ]
def bubblesort():
    for i in range(len(num)): # or i can be started from behind: (len(num)-2,-1,-1)
        for j in range(0, len(num)-1):
            if num[j]>num[j+1]:
                num[j], num[j+1] = num[j+1] , num[j]
    return (num)

print(bubblesort())


# recursion

def bubblesort(num, i, j):
    if i==len(num):
        return (num)
    if j == len(num)-1:
        return bubblesort(num, i+1 , 0)
    if num[j]>num[j+1]:
        num[j], num[j+1] = num[j+1] , num[j]
        return bubblesort(num, i , j+1)
    else:
        return bubblesort(num, i , j+1)
    return bubblesort(num, i+1 , 0)

num = [ 5, 7, 8, 4,1,6,9,2 ]
print(bubblesort(num, 0, 0))

# alternative : much efficient

def bubble_sort_recursive(num, i=None, j=None, swapped=False):
    if i is None or j is None:
        i = 0
        j = 0
        swapped = False  # Initialize the flag for the brand new pass
        
    if i == len(num):
        return num
        
    # When j reaches the end of its optimized pass window...
    if j == len(num) - 1 - i:
        # If a whole pass happened and NO swaps occurred, the list is sorted!
        if not swapped : 
            return num
        # Reset j to 0, increment i, and reset swapped to False for the next pass
        return bubble_sort_recursive(num, i + 1, 0, swapped=False)
        
    if num[j] > num[j+1]:
        num[j], num[j+1] = num[j+1], num[j]
        # A swap happened! Set swapped=True and pass it to the next step
        return bubble_sort_recursive(num, i, j + 1, swapped=True)
        
    # No swap happened on this step, so forward the current 'swapped' state
    return bubble_sort_recursive(num, i, j + 1, swapped)

my_list = [5, 7, 8, 4, 1, 6, 9, 2]
print(bubble_sort_recursive(my_list))

# Output: [1, 2, 4, 5, 6, 7, 8, 9]