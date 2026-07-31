# advanced python

# lect 6

# reverse digits

num = 1234 # dont change input

def reversedigits(n, newnum): # recursion method
    if (n==0):
        print(int(newnum/10))
        return
    n1=n%10
    newnum=newnum+(n1)
    newnum=newnum*10
    n=n//10
    reversedigits(n, newnum)
    
reversedigits(1234, 0) # even if u try with 120 or 100 this code will work


# so TC : O(log10(N))