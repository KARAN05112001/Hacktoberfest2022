# Program to check if a number is prime or not

num = 5

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for j in range(2,num):
       if (num % j) == 0:
           print(num,"is not a prime number")
           print(j,"times",num//j,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
