#Program to check if a number is armstrong

n = int(input("Enter the number"))

number = str(n)
a = len(number)
output = 0

for i in number:
    output = int(output+int(i)**a)
if output == n:
    print("Number is Armstrong")
else:
    print("Number is not armstrong")