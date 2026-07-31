# advanced python

# lect 6

# reverse digits

num = 1234 # dont change input

def reversedigits(n, newnum): # recursion method
    if (n==0):
        print(int(newnum/10))
        if (a1==int(newnum/10)):
            print(f"{a1} and {int(newnum/10)} are palindrome")
            return
        else:
            print(f"{a1} and {int(newnum/10)} are not a palindrome")
        return
    n1=n%10
    newnum=newnum+(n1)
    newnum=newnum*10
    n=n//10
    reversedigits(n, newnum)
    
a1=1234
reversedigits(a1, 0) # even if u try with 120 or 100 this code will work

# so TC : O(log10(N))

# alternative

n =121
s1=str(n)
a1=list(s1)
a1.reverse()
print(a1)
a2="".join(a1)
print(a2)
a2=int(a2)
print( a2==n, "-- false means not a palindrome, true means is a palindrome")

# alternative

n =121
print(str(n) == str(n)[::-1])