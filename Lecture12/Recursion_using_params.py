# advanced python

# lect 12

# recursion : using params

# q1 : print "15" 3 times using recursion

def printnum(num, i):
    if i == 3: # here restrictions might come as what if we are asked to print 9 times
        return
    print(num)
    return printnum(num, i+1) # tail recursion : meaning first code part executed then func was called
printnum(15, 0)

# q2 : print "hello" 4 times using recursion

# using tail recursion

def printnum(num, i):
    if i == 0: # here restrictions might come as what if we are asked to print 9 times
        return
    print(num)
    return printnum(num, i-1) # here i can be reduced uptil 0
printnum(15, 4) # so it can priny i times

# so TC : O(n+1) ~ O(n)
# so SC : O(n+1) ~ O(n)

# print 1 to 5 using recursion

def printnum(num):
    if num == 6: # basic condn
        return
    print(num)
    return printnum(num+1) # self call
printnum(1)


# above one using head recursion

def printnum(num):
    if num == 0: # basic condn
        return
    printnum(num-1) # self call
    print(num)
printnum(5)