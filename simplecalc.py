#Program of a simple calculator
n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
a = input("Select the operator(+,-,*,/)")
if a == '+':
    print(f"Sum is {n1 + n2}")
elif a == '-':
    print(f"Difference is {n1-n2}")
elif a == '*':
    print(f"Product is {n1*n2}")
elif a == '/':
    print(f"Division is {n1/n2}")
