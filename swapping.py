#Program to swap two variables
a = int(input("Enter the value of first variable 'a"))
b = int(input("Enter the value of second variable 'b"))
print(f"Value of a and b before swapping {a} and {b}")
a = a * b
b = a // b
a = a // b
print(f"Value of a and b after swapping {a} and {b}")