# advanced python

# lect 7

# armstrong num

num = 153 # dont change input

def countdigits(n, count):
    if (n==0):
        return (count)
    count+=1
    n=n//10
    return countdigits(n, count)

def armstrongnum(n,a2, ans): # recursion method
    if (n==0):
        print(ans, "is the armstrong")
        if (ans==a1):
            print(f"{ans} and {a1} are armstrong num")
            return
        else:
            print(f"{ans} and {a1} are not armstrong num")
            return
        
        return
    n1=n%10
    m1=n1**a2
    ans=ans+m1
    n=n//10
    armstrongnum(n, a2, ans)
    
a1=153
a2=countdigits(a1, 0)
print(a2)
armstrongnum(a1, a2, 0)# even if u try with 120 or 100 this code will work

# so TC : O(log10(N))


# alternative

from math import *
num=153

n=153

lengthofn=int((len(str(n))))

ans = 0
for i in str(n):
    m=pow(n%10, lengthofn)
    n=n//10
    ans+=m
print (int(ans))
if (ans == num):
    print ("is a palidrome")
else:
    print ("is not a palidrome")

# more advance python practice notes coming up