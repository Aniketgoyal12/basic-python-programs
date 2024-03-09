#Program to print multiplication table 
n = int(input("Enter the number"))
for i in range(1,11,1):
    print(f"{n} * {i} = {(n*i)}")