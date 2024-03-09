#Program to check if a number is prime

n = int (input("Enter the number"))
count = 0
for i in range(1,n+1,1):
    if n%i != 0:
        count =+ 1
if count == 2:
    print("Number is  prime")
else:
    print("Number is not prime")


APPROACH 2:

n = int (input("Enter the number"))
count = 0
for i in range(2,n+1,1):
    if n%i != 0:
        count =+ 1
if count == 1:
    print("Number is  prime")
else:
    print("Number is not prime")
