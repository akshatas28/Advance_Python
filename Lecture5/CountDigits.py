# advanced python

# lect 5

# count digits

num = 5873 # dont change input

def countdigits(n, count): # recursion method
    if (n==0):
        print (count)
        return
    count+=1
    n=n//10
    countdigits(n, count)
        
    

countdigits(5873, 0)


import math

num = 5873
# math.log10(5873) is roughly 3.768. math.floor drops the decimal to 3. Adding 1 gives 4.
count = math.floor(math.log10(num)) + 1
print(count)  # Outputs: 4

# whenever n//10 is operation : TC includes that //num : that number must be the base of log func

# so TC : O(log10(N))