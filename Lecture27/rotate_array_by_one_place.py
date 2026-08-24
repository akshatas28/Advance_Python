# advanced python

# lect 27 : rotate array by one place

# simple

value=1
num = [ 5,-2,3,9,0,6,10,7 ]
value = value % len(num)

# num[:] = [num[-1]]+num[0:n-1]
num[:] = [num[-value]]+num[0:len(num)-value]
print(num)

# else

num = [ 5,-2,3,9,0,6,10,7 ]
temp=num[len(num)-1]
for i in range(len(num)-2,-1,-1):
    num[i+1]=num[i]
num[0] = temp
print(num)