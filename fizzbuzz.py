#Program to print numbers between a range if number is divided by 3 print fizz if number is divisible by 5 print buzz if divisible by both print fizzbuzz
lower = int(input("Enter the lower number"))
upper = int(input("Enter the upper number"))
for i in range(lower,upper+1):
    if i%3 == 0 and i%5 == 0:
        print('FIZZBUZZ')
    elif i%3 == 0:
        print('FIZZ')
    elif i%5 == 0:
        print('BUZZ')
    else:
        print(i)