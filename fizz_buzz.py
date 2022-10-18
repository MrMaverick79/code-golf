for i in range(1,101):a,b="Fizz","Buzz";c=lambda i:i%15<1and a+b or i%3<1and a or[i,b][i%5<1];print(c(i))
