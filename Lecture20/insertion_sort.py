# advanced python

# lect 20 : insertion sort : 

num = [ 5, 7, 8, 4,1,6,9,2 ]
a1=[]
a1.append(num[0])
def insertionsort():
    for i in range(1, len(num)): # or i can be started from behind: (len(num)-2,-1,-1)
        for j in range(0, len(a1)):
            if num[i]<a1[j]:
                temp=a1[j]
                a1[j]=num[i]
                num[i] = temp
        a1.append(num[i])
    return (a1)

print(insertionsort())

# Time (O(n)) always | Space (O(n)) | High memory write overhead.

# second type

num = [ 5, 7, 8, 4,1,6,9,2 ]
def insertionsort():
    for i in range(1, len(num)): # or i can be started from behind: (len(num)-2,-1,-1)
        for j in range(i, 0, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1] , num[j]
            else:
                break
    return (num)

print(insertionsort())

# Time (O(n)) always | Space (O(1)) | High memory write overhead.

# recursion

def insertionsort(num, i, j):
    if i==len(num):
        return (num)
    if j == 0:
        return insertionsort(num, i+1 , i+1)
    if num[j]<num[j-1]:
        num[j], num[j-1] = num[j-1] , num[j]
        return insertionsort(num, i , j-1)
    else:
        return insertionsort(num, i+1 , i+1)

num = [ 5, 7, 8, 4,1,6,9,2 ]
print(insertionsort(num, 1, 1))

# alternative : much efficient

def insertion_sort_recursive(num, i=None, j=None, swapped=False):
    if i is None or j is None:
        i = 1
        j = 1
        swapped = False  # Initialize the flag for the brand new pass
    if i == len(num):
        return num
    if j == 0:
        if not swapped : 
            return num
        return insertion_sort_recursive(num, i + 1, i+1, swapped=False)
    if num[j] < num[j-1]:
        num[j], num[j-1] = num[j-1], num[j]
        return insertion_sort_recursive(num, i, j - 1, swapped=True)
    return insertion_sort_recursive(num, i+1, i+ 1, swapped)

my_list = [2, 1, 5, 4, 3]
print(insertion_sort_recursive(my_list))

# Output: [1, 2, 3, 4, 5]

# second one : flagless

def insertion_sort_recursive(num, i=None, j=None):
    if i is None or j is None:
        i = 1
        j = 1
    if i == len(num):
        return num
    if j == 0:
        return insertion_sort_recursive(num, i+1, i+ 1)
    if num[j] < num[j-1]:
        num[j], num[j-1] = num[j-1], num[j]
        return insertion_sort_recursive(num, i, j - 1)
    return insertion_sort_recursive(num, i+1, i+ 1)

my_list = [2, 1, 5, 4, 3]
print(insertion_sort_recursive(my_list))