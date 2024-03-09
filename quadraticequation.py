#Program to solve the quadratic equation
a = int(input("Enter the coefficient of x^2"))
b = int(input("Enter the coefficient of x "))
c = int(input("Enter the constant term"))

d1 = int(((-b + ((b**2) - 4*a*c)**0.5)/2*a))
d2 = int(((-b - ((b**2)-4*a*c)**0.5)/2*a))
print(d1,d2)