# advanced python

# lect 2

# TLE = Time Limit Exceeded error

# depends on 2 properties = Time Limit + constrains

# 1. time limit : 1 sec = 10^8 operations
# 2. constants : always provided in code question
# example below

list = [ 5, 6 ,7, 30, 67, 87 ]
constraint : 1< N < 10^5

# now if for above code the time limit is n^2

# for 10^5 input constraints = 10^10 will be the limit

# so for 1 sec = 10^8 operations, for 10^10 operations = 100 sec will be needed

# this will take program to run for many secs which is not good practice. thus error comes : TLE

# so whenever TLE comes : try to lower down number of operations 

# best Tc cases : O(n), O(n log n), O(log n)