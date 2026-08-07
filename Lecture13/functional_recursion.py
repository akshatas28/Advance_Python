# advanced python

# lect 13

# recursion : functional recursion

# q1 : sum using parametrized recursion 

def printsum(sum, i, n):
    if i > n:
        print (sum)
        return
    printsum(sum+i, i+1, n)
printsum(0, 0, 10)

# functional recursion : 

def printsum(n):
    if n ==1:
        return 1
    return n + printsum(n-1)
    
print(printsum(10))


# so TC : O(n)
# so SC : O(n) ~ stack space