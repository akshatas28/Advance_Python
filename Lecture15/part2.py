# advanced python

# lect 15 : part 2

# recursion : reverse an array

num =[ 5, 7, 3, 2, 6, 1, 5, 9 ]

# two pointer method

def printrevlist(num, left=None, right=None, num1=None):
    if num==[]:
        return []
    if num1 is None:
        num1=list(num)
    if num1 == []:
        return []
    if left is None:
        left=0
    if right is None:
        right=len(num1)-1
    if left >= right:
        return num1
    num1[left], num1[right] = num1[right], num1[left]
    return printrevlist(num, left+1,right-1, num1)

print(printrevlist([ 5, 7, 3, 2,6,1, 5,9 ]))

# and if somebody wants to swap only few elements of lisy, they can just introduce left and right value

def printrevlist(num, left=None, right=None, num1=None):
    if num==[]:
        return []
    if num1 is None:
        num1=list(num)
    if num1 == []:
        return []
    if left is None:
        left=0
    if right is None:
        right=len(num1)-1
    if left >= right:
        return num1
    num1[left], num1[right] = num1[right], num1[left]
    return printrevlist(num, left+1,right-1, num1)

print(printrevlist([ 5, 7, 3, 2,6,1, 5,9 ], 2, 5))

#reversal of str

def prtrevstr(str1, left=None, right=None, str1copy=None):
    if str1=="":
        return ""
    if str1copy is None:
        str1list=str1.lower() # str1copy=str(str1) or str1copy=str1[:]
        str1copy=list(str1list)
    if str1copy == "" :
        return ""
    if left is None:
        left=0
    if right is None:
        right=len(str1copy)-1
    if left >= right:
        return ("".join(str1copy))
    str1copy[left], str1copy[right] = str1copy[right], str1copy[left]
    return prtrevstr(str1, left+1,right-1, str1copy)

print(prtrevstr("akshata"))