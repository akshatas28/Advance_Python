# advanced python

# lect 9

# store freq in dict

num = [1,2,3,4,5,1,2,3,1,2,3] # dont change input
dict1={}
count=1
for i in num:
    if (i in dict1):
        dict1[i]+=1
    else:
        dict1[i]=1
print (dict1)

# so TC : O(N)


# alternative

num = [1,2,3,4,5,1,2,3,1,2,3] # dont change input
def checkfreqindict(n, dict1):
    if (n==len(num)):
        return dict1
    m=num[n]
    if (m in dict1):
        dict1[m]+=1
        return checkfreqindict(n+1, dict1)
    else:
        dict1[m]=1
        return checkfreqindict(n+1, dict1)

print(checkfreqindict(0, {}))

# so TC : O(N)
# so SC : O(k) : k is number of keys

# alternative

num = [1,2,3,4,5,1,2,3,1,2,3] # dont change input
dict1={}
for i in range(0,len(num)):
    dict1[num[i]]=dict1.get(num[i],0)+1
print (dict1)

# so TC : O(N)
# so SC : O(k) : k is number of keys