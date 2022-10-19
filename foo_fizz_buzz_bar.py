# Print the numbers from 1 to 1,000 inclusive, each on their own line.

# If, however, the number is a multiple of two then print Foo instead, if the number is a multiple of three then print Fizz, if the number is a multiple of five then print Buzz, and if the number is a multiple of seven then print Bar.

# If multiple conditions hold true then all replacements should be printed, for example 15 should print FizzBuzz.   

for i in range(1,1001):
 a,b,c,d,s='Foo','Fizz','Buzz','Bar',""
 if i%2<1:s+=a
 if i%3<1:s+=b
 if i%5<1:s+=c
 if i%7<1:s+=d
 x=lambda s:len(s)and s or i;print(x(s))

