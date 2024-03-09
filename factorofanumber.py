#Program to find the factor of a number
n = int(input("Enter the number to find its factor"))
for i in range(1,n+1,1):
    if n%i == 0:
        print(i,end=' ')