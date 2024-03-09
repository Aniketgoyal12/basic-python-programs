#Program to print fibonacci series
n = int(input("Enter the number of elements "))
a = 0
b = 1
print(a,b,end=' ')
for i in range(2,n):
    c= a+b
    print(c,end=' ')
    a = b
    b = c