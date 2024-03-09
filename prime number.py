#Program to check if a number is prime

n = int (input("Enter the number"))
count = 0
for i in range(2,n,1):
    if n%i != 0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")