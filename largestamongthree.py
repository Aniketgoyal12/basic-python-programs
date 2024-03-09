#Program to find the largest among three numbers
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))
if (n1 > n2) and (n1 > n3):
    largest = n1
elif (n2 > n1) and (n2 > n3):
    largest = n2
else:
    largest = n3
print(f"{largest} is the largest number")