# advanced python

# lect 26 : remove duplicated from array in place

# simple

# using while loop

num = [1, 2, 2]
i=0
n=len(num)
while i <n-1:
    if num[i]<num[i+1]:
        i+=1
    elif num[i]==num[i+1]:
        n-=1
        num.pop(i)
print(num)

# else

num=[3,5,6,8,9,10,20]
count=0
for i in range(len(num)-1):
    if num[i]<=num[i+1]:
        count+=1
    else:
        print("array is not sorted")
        break
if count==len(num)-1:
    print("array is sorted")

# recursion

#num=[3,5,6,8,9,10,20]

#num= [1,1,1,2,3,4,4,7,9,9,9,10]

#num = [1, 2, 3, 4, 10, 10, 10, 10]

num = [1, 2, 2]

def removeduplicates(num, i ):
    if i==len(num)-1:
        return num
    if len(num)<=1:
        return num
    if num[i]<num[i+1]:
        return removeduplicates(num, i+1)
    elif num[i]==num[i+1] :
        num.remove(num[i])
        return removeduplicates(num, i)
       
print(removeduplicates(num, 0 ))

# leetcode solution


num=[1, 2, 2, 2, 3]
index=1
count=0
for i in range(1, len(num)):
    if num[i] != num[i-1] :
        num[index] = num[i]
        index+=1
    else:
        count+=1
#num[:] = [x for x in num if x != '_']
num[index:] = ["_"] * count
print(num)

# using dictionary

num=[1, 2, 2, 2, 3]
dict1={}
index=0
count=0
for i in range(0, len(num)):
    if num[i] not in dict1:
        dict1[num[i]] = 0
    else:
        count+=1
for j in dict1:
    num[index] = j
    index+=1
num[index:] = ["_"] * count
print(num)

# two pointer

num = [1, 2, 2, 3, 4, 5, 5]
#num=[1, 2, 2, 2, 3]
index=0

for j in range(1, len(num)):
    if num[j] !=num[index]:
        index+=1
        num[index] , num[j] = num[j] , num[index]

num[index+1:] = ["_"] * (len(num)-1-index)
print(index)
print(num)