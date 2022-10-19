# An evil number is a non-negative number that has an even number of 1s in its binary expansion.

# Print all the evil numbers from 0 to 1,000 inclusive, each on their own line. 

#Solution:
for j in range(1001):
 x,c=bin(j),0
 for i in x[::-1]:
  if i=='1':c+=1
 if c%2<1:print(j)