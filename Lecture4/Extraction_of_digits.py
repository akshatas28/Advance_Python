# advanced python

# lect 4

# Extraction of digits

# can be used for : COUNT DIGITS , REVERSE , PALINDROME , ARMSTRONG

num = 5873 # dont change input

def check(n): # recursion method
    if (n==0):
        return 
    q = n%10
    print(q)
    n = n//10
    check(n)
    

check(5873)