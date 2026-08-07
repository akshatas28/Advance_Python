# advanced python

# lect 14

# recursion : functional recursion

# q1 : factorial using parametrized recursion 

def printfact(fact, i, n):
    if i > n:
        print (fact)
        return
    printfact(fact*i, i+1, n)
printfact(1, 1, 10)

# functional recursion : 

def printfact(n):
    if n ==1 or n ==-1:
        return 1
    return n * printfact(n-1)
    
print(printfact(10))


# so TC : O(n)
# so SC : O(n) ~ stack space