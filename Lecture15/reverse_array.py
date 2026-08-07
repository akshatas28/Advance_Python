# advanced python

# lect 15

# recursion : reverse an array

num =[ 5, 7, 3, 2, 6, 1, 5, 9 ]

# simple one 

num =[ 5, 7, 3, 2, 6, 1, 5, 9 ]
num.reverse()
print(num)

# using recursion

num =[ 5, 7, 3, 2, 6, 1, 5, 9 ]

def printrevlist(num1, i):
    if i ==-1:
        return num1
    num1.append(num[i])
    return printrevlist(num1, i-1)

num1=[]
print(printrevlist(num1, (len(num)-1)))

# alternative

def printrevlist(num1, num):
    if num==[]:
        return num1
    num1.append(num[-1])
    return printrevlist(num1, num[:-1])


print(printrevlist([], [ 5, 7, 3, 2, 6, 1, 5, 9 ]))

# alternative : 

def printrevlist(num, num1=None):
    if num1 is None:
        num1=[]
    if num==[]:
        return num1
    num1.append(num[-1])
    return printrevlist(num[:-1],num1)


print(printrevlist([ 5, 7, 3, 2, 6, 1, 5, 9 ]))

# not a perfect approach but can try only for one list

def printrevlist(num, num1=[]):
    if num==[]:
        return num1
    num1.append(num[-1])
    return printrevlist(num[:-1],num1)


print(printrevlist([ 5, 7, 3, 2, 6, 1, 5, 9 ]))



# reversing only mid elements of list -


def printrevlist(num, i=None, num1=None, num2=None):
    if num1 is None:
        if (int(len(num))%2==0):
            a=int((len(num))/2)
            b=int(a/2)
            num1=num[b:-b]
        else:
            a=int((len(num))/2)
            b=int(a/2)
            num1=num[b:len(num)-b]
    if num2 is None:
        num2=[]
    if i==len(num):
        return num2
    if i is None:
        i=0
    if (int(len(num))%2 ==0):
        mon=int(len(num))/2
        mmon=int(mon/2)
        if num1:
            if i>=mmon:
                num2.append(num1[-1])
                return printrevlist(num, i+1,num1[:-1], num2)
    else:
        mon=int(len(num))//2
        mmon=int(int(mon)/2)
        if num1:
            if i>=mmon:
                num2.append(num1[-1])
                return printrevlist(num, i+1,num1[:-1], num2)
    num2.append(num[i])
    return printrevlist(num, i+1,num1, num2)


print(printrevlist([ 5, 7, 3, 2, 6, 1, 5, 9,78 ]))

# alternative by AI -

# Reversing only mid elements of a list dynamically (Works for ALL sizes, Odd & Even)

def printrevlist(num, i=0, num1=None, num2=None, b=None, end_b=None):
    # Initialize boundary pointers ONLY ONCE on the very first call
    if num1 is None:
        num2 = []
        
        # Using integer division (//) to avoid unnecessary float conversions
        mid_point = len(num) // 2
        b = mid_point // 2
        
        # Dynamic calculation of where the middle zone ends
        end_b = len(num) - 1 - b
        
        # Slice the middle elements cleanly
        num1 = num[b:end_b+1]

    # Base case: Hand back the constructed list once we parse the whole array
    if i == len(num):
        return num2

    # Dynamic Zone Check: If current index falls between our start and end boundaries
    if b <= i <= end_b:
        num2.append(num1[-1])
        return printrevlist(num, i + 1, num1[:-1], num2, b, end_b)

    # Outer Zone Check: Keep elements exactly as they are
    num2.append(num[i])
    return printrevlist(num, i + 1, num1, num2, b, end_b)

# Test cases to prove it works dynamically
print("Even (8 elements):", printrevlist([5, 7, 3, 2, 6, 1, 5, 9]))
print("Odd  (9 elements):", printrevlist([5, 7, 3, 2, 6, 1, 5, 9, 78]))
print("Large Odd (11 elements):", printrevlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))