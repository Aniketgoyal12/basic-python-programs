#Program to swap two variables
a = int(input("Enter the value of first variable 'a"))
b = int(input("Enter the value of second variable 'b"))
print(f"Value of a and b before swapping {a} and {b}")
a = a * b
b = a // b
a = a // b
print(f"Value of a and b after swapping {a} and {b}")

APPROACH 2: USING ADDITION AND SUBTRACTION

a = int(input("Enter the value of first variable 'a"))
b = int(input("Enter the value of second variable 'b"))
print(f"Value of a and b before swapping {a} and {b}")
a = a  b
b = a - b
a = a - b
print(f"Value of a and b after swapping {a} and {b}")

APPROACH 3: USING THIRD VARIABLE

a = int(input("Enter the value of first variable 'a"))
b = int(input("Enter the value of second variable 'b"))
print(f"Value of a and b before swapping {a} and {b}")
c = a 
a = b
b = c
print(f"Value of a and b after swapping {a} and {b}")

APPROACH 4: WITHOUT USING A THIRD VARIABLE

a = int(input("Enter the value of first variable 'a"))
b = int(input("Enter the value of second variable 'b"))
print(f"Value of a and b before swapping {a} and {b}")
a,b = b,a
print(f"Value of a and b after swapping {a} and {b}")
