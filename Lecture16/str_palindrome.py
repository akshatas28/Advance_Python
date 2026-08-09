# advanced python

# lect 16

# recursion : check if str is palindrome

num =[ 5, 7, 3, 2, 6, 1, 5, 9 ]

# two pointer method

def prtpalindrome(str1, left=None, right=None):
    if str1=="":
        return ""
    if left is None or right is None:
        str1 = str1.lower() # Safely creates the lowercase version ONCE
        left = 0
        right = len(str1) - 1
    if str1[left] !=str1[right]:
        return False
    if left >= right:
        # newstr = ("".join(str1copy)) : used for returning a str if needed to be showcased
        return True
    # str1copy[left], str1copy[right] = str1copy[right], str1copy[left]
    return prtpalindrome(str1, left+1,right-1)

print(prtpalindrome("Racecar"))

# below code would work but it would be memory inefficient: because evey time a new str would be created and traversed

def printrevlist(str1):
    str1 = str1.lower()
    
    # Base Case: An empty string or single letter is always a palindrome
    if len(str1) <= 1:
        return True
        
    # Check if it starts and ends with the same character
    if str1.endswith(str1[0]):
        # Strip the first and last character off, and pass the smaller string down!
        return printrevlist(str1[1:-1]) 
    else:
        return False

# iterative approach

str1="motom"
str1=str1.lower()
for i in range(len(str1)):
    left = i
    right = len(str1)-1-i
    if str1[left] !=str1[right]:
        print ("not a palindrome")
        break
    if left>=right:
        print ("is a palindrome")
        break