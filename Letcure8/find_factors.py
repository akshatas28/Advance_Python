# advanced python

# lect 8

# find factors num

num = 20 # dont change input

def factors(n, result):
    if (n==num):
        result.append(n)
        return
    if num%n==0:
        result.append(n)
        factors(n+1, result)
        return result
    return factors(n+1, result)

print(factors(1,[]))

# so TC : O(N)


# alternative

num =20
result=[]
for i in range(1,num+1):
    if (num%i==0):
        result.append(i)
print(result)

# so TC : O(N)
# so SC : O(k) : k is number of factors

# alternative

num =20
result=[]
mid = num/2
for i in range(1,int(mid+1)):
    if (num%i==0):
        result.append(i)
result.append(num)
print(result)

# so TC : O(N/2) ~ O(N)
# so SC : O(k) : k is number of factors

# alternative : sq rt method

from math import *

num =36
result=[]
for i in range(1,int(sqrt(num))):
    if (num%i==0):
        result.append(i)
        if (num/i!=i):
            result.append(int(num/i))
result.append(int(sqrt(num)))
result.sort()
print(result)


# sorting TC : O(K logK) : K number of factors
# TC : O(K logK) + O(sqrt N) = O(sqrt N)