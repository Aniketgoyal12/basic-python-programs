#Program to find the sum of natural numbers
n = int(input("Enter the number of (upto which we need to find the sum)"))
sum = 0
for i in range(0,n+1,1):
    sum += i
print(sum)