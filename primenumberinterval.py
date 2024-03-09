#Program to print prime number in an interval
n = int(input("Enter the number upto which you want to print the number"))
count = 0
for i in range(2,n+1,1):
    if n%i !=0:
        count += 1
for j in range (1,n):
    if count == 1:
        print(j,end='\n')

#Not completed this code yet
