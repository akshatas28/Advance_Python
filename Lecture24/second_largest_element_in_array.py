# advanced python

# lect 24 : second largest element in array

# normal one

num=[ 55,32,-97,99,3,67 ]
num.remove(max(num))
print(max(num))

# else

num=[ 55,32,-97,99,3,67 ]
num.sort()
print(num[-2]) # else: print(num[len(num)-2])

# using sorting
# using exchange sort

num=[ 55,32,-97,99,3,67 ]
for i in range(0, len(num)-1):
    for j in range(i+1,  len(num)):
        if num[i]>num[j]:
            num[i], num[j] =num[j], num[i]

print(num[-2])

num=[ 55,32,-97,99,3,67 ]

# using bubble sort

for i in range(0, len(num)):
    for j in range(0,  len(num)-1):
        if num[j]>num[j+1]:
            num[j], num[j+1] =num[j+1], num[j]

print(num[-2])

# using for loop

tempresult=0
num=[ 55,32,-97,99,3,67 ]
result = 0
for i in range(len(num)):
    if result <num[i]:
        result=num[i]
for i in range(len(num)):
    if tempresult <num[i] and num[i]<result :
        tempresult=num[i]
print(tempresult)

# using simple loop

num=[ 55,32,-97,99,3,67 ]
if num[0]<num[1]:
    larg=num[1]
    seclarg=num[0]
else:
    seclarg=num[1]
    larg=num[0]

for i in range(2, len(num)):
    if num[i]<larg:
        if num[i]>seclarg:
            seclarg=num[i]         
    else:
        if num[i]>larg:
            seclarg=larg
            larg=num[i]       
print(seclarg)

# using recursion

def seclarge(num, larg, seclarg, i):
    if len(num) < 2: return None
    if i==len(num):
        return seclarg
    if num[i]<larg : 
        if num[i] >seclarg :
            return seclarge(num, larg, num[i], i+1)
        else:
            return seclarge(num, larg, seclarg, i+1)
    else:
        if num[i] > larg:
            return seclarge(num, num[i], larg, i+1)
        else:
            return seclarge(num, larg, seclarg, i+1)

num=[ 55,32,-97,99,3,67 ]
if num[0]<num[1]:
    larg=num[1]
    seclarg=num[0]
else:
    seclarg=num[1]
    larg=num[0]

print(seclarge(num, larg, seclarg, 2))