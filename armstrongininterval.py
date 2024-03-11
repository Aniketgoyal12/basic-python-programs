#Program to print armstrong numbers in an interval
lower = int(input("Enter the lower value of the interval"))
upper = int(input("Enter the upper value of the interval"))

for i in range(lower,upper+1,1):
    if i >1 :
        k = str(i)
        n = len(k)
        output = 0
        for j in k :
            output = int(output + int(j)**n)
            if output == i:
                print(i,end='\n')