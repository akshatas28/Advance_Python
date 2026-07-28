# advanced python

# lect 3

# Time complexity of most common used expressions

# LIST

# ammortised worst case : example : take list of size 4, now start filling it, for every fill TC = O(1), but for 5th element filling : it will copy thr existing list with greater size : say 8 -- then again to fill 6,7,8 : it takes O(1) : so TC becomes : 1+1+1+1+N+1+1+1+N : IN THIS WAY : O(N) : Worst case

# operation : copy , pop intermediate , insert mid , delete , iteration, x in s (membership) , delete slice , min max : O(n) : avg case
# operation : append , pop last , get , set , length : O(1) : avg case
# operation : get slice : k - length of slice 


# SET 

# operation : X in S : O(1)

# DICT
# operation : key in dict , get , set , delete : O(1)
# operation : copy , iteration : O(n)