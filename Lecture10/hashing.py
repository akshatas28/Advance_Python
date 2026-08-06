# advanced python

# lect 10

# hashing concept : prestoring values in ds and fetching it

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
dict1={}
for i in m:
    count=0
    for (j) in (n):
        if j==i:
            count+=1
        dict1[i]=count
print (dict1)

# so TC : O(n*m) : which becomes 10^8*10^8=10^16 : TLE error
# SC : O(k) : k is number of keys


# alternative

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

dict1={}
for i in m:
    count=0
    if i >10:
        dict1[i]=count
    else:
        for j in range(0,10): # 10 can be replaced by len(n) but TC will blast off
            if n[j]==i:
                count+=1
            dict1[i]=count
print (dict1)

# so TC : O(m)
# so SC : O(k) : k is number of keys

# alternative

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
count=0
hashmap={}
dict1={}
for i in range(1,11):
    if i in n:
        count=n.count(i)
        hashmap[i] = count
print (hashmap)

for j in m:
    if j in hashmap:
        dict1[j]=hashmap.get(j)
    else:
        dict1[j]=0
print(dict1)

# so TC : (O(n^2 + m)).
# so SC : O(k) : k is number of keys


# alternative


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
i=1
hashlist, dict1={} , {}
def hashinglist(i,n,hashlist):
    if i >10:
        return hashlist
    if i in n:
        hashlist[i] =n.count(i)
    return hashinglist(i+1,n,hashlist)

def checkminn(m, j, b, dict1):
    if j==len(m):
        return dict1
    if m[j] in b:
        dict1[m[j]]=b.get(m[j])
    else:
        dict1[m[j]]=0
    return checkminn(m, j+1, b, dict1)

b = (hashinglist(i,n,hashlist))
print(checkminn(m, 0, b, dict1))

# so TC : (O(n+ m)).
# so SC : O(k+m) : k is number of keys


# new question with str

s = "azyxyyzaaaa"
m = ["d","a","y","z"]
count=0
i=0
j=0
dict1={}

def checkfreqs(s, m, count, i, j):
    if i==len(s):
        return checkfreqs(s, m, 0, 0, j+1)
    if j==len(m):
        return dict1
    if m[j] in s:
        if m[j] == s[i]:
            count+=1
        dict1[m[j]]=count
        return checkfreqs(s, m, count, i+1, j)
    else:
        dict1[m[j]]=0
        return checkfreqs(s, m, count, i, j+1)

print(checkfreqs(s, m, count, i, j))

# so TC : (O(s*m)).
# so SC : O(k) : k is number of keys

# alternative with hashset

import string

alphabet = string.ascii_lowercase

s = "azyxyyzaaaa"
m = ["d","a","y","z"]
count, i,j=0,0,0
hashlist, dict1={} , {}
def hashinglist(alphabet, i,s,hashlist):
    if i ==26:
        return hashlist
    if alphabet[i] in s:
        hashlist[alphabet[i]] =s.count(alphabet[i])
    return hashinglist(alphabet, i+1,s,hashlist)

def checkmins(ltrdict, m, s, j):
    if (j==len(m)):
        return dict1
    if m[j] in ltrdict:
        dict1[m[j]]=ltrdict.get(m[j])
    else:
        dict1[m[j]]=0
    return checkmins(ltrdict, m, s, j+1)

ltrdict= (hashinglist(alphabet,i,s,hashlist))

print(checkmins(ltrdict, m, s, j))

# alternative for efficiency

s = "azyxyyzaaaa"
m = ["d","a","y","z"]

# Step 1: Scan string S exactly ONCE -> True O(S) time, O(26) space
ltrdict = {}
for char in s:
    ltrdict[char] = ltrdict.get(char, 0) + 1

# Step 2: Extract targets from M -> True O(M) time, O(M) space
dict1 = {}
for target in m:
    dict1[target] = ltrdict.get(target, 0)

print(dict1) # {'d': 0, 'a': 5, 'y': 3, 'z': 2}