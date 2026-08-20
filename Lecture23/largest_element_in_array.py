# advanced python

# lect 23 : largest element in array

# normal one

num=[ 55,32,-97,99,3,67 ]

print(max(num))

# using normal code : for loop

num=[ 55,32,-97,99,3,67 ]
result=num[0] # result = float("-inf") : to start the result from minus infinity
for i in range(1, len(num)):
    if result<num[i]:
        result=num[i]
print(result)

# using while loop

num=[ 55,32,-97,99,3,67 ]
j=1
result=num[0]
while j<len(num):
    if result<num[j]:
        result=num[j]
    j+=1
print(result)

# recursion

def largest(num, i, result):
    if i == len(num):
        return result
    if result < num[i]:
        return largest(num, i+1, num[i])
    else:
        return largest(num, i+1, result)

num=[ 55,32,-97,99,3,67 ]
print(largest([ 55,32,-97,99,3,67 ], 1, num[0]))