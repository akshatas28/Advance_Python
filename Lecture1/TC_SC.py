# advanced python

# lect 1

# Time complexity, SPace complexity

# 3 rules for TC

# 1. Always calculate worst case TC
# 2. Avoid constants
# 3. Avoid lower bound values
# NOTATION : Big-Oh (N) --> N : number of operations for inputs N : --> example : O(n)

# TC = O(8N^6 + 3N^2 + 15) --> here 15 can be ignored : why to ignore but? yes because if one considers N=10^5 then just by calculating : 10^5*6 which becomes 10^30 --> infront of 10^30 , 15 will be negligible : so one of the rules

# comparing N^2 to N^6 --> N^2 is negligible so avoiding it. 

# to build website : its easy to build for 100 people but difficult for 10000 people, but always choose 10000 people scenario as taking worst case possiblity will help deviate and work with max possibility

# different types of TC : 
# Big-oh notation : O() --> worst case, upper bound
# theta notation : theta sign() --> avg case, mid bound
# omega notation : omega sign() --> best case, lower bound

# how to calculate : O()

# eg: below

for i in range(1,n+1):
    for j in range(1,n+1):
        pass
# here : for 1st i loop : j runs N times = N*1
# for 2nd i loop : j runs N times = N*2 
# so total for N i loops : j runs N times = N*N

# so TC becomes = O(N^2)

# space complexity : memory space

# SC = Auxiliary space + input space

# auxiliary space = the new vars introduced during writing code

# input space = the input needed to run a program

# never edit input vars unless asked externally 

# example code

x = 8
y = 15
z = 54
total = x+y+z
print (total)


# in above example : total --> auxiliary space

# x,y,z --> input space

# for array/list : SC = O(n)