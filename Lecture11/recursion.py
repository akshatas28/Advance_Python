# advanced python

# lect 11

# recursion : functiom callibg itself but more imp : a funct reducing itself to th3 smalled executabke code part and executing itself

# Basic syntax: 

def func():
    if condition: # know as mandate basuc condition else recusion loop will continue to execute unless 987 limit is reached then we will get Stach Overflow error
        return # needed to exit from func
    #here the executable code part can be written
    
func() # calling the func is necessary else the func part will not get executed

# q1 : print "hello" 4 times using recursion

def printhello(i):
    if i == 4:
        return
    print("hello")
    return printhello(i+1) # tail recursion : meaning first code part executed then func was called
printhello(0)

# q2 : print "hello" 4 times using recursion

# using head recursion

def printhello(i):
    if i == 4:
        return
    printhello(i+1) # is we used return : it exits from code, hence not executing further commands
    print("hello")
printhello(0)

# so TC : O(n+1) ~ O(n)
# so SC : O(n+1) ~ O(n)