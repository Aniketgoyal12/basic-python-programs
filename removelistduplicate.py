#Program to remove duplicate element from a list

#Let us suppose we have a list l with some duplicate elements

l = ['apple','banana','apple','strawberry','mango','blackberry']
a = input("Enter the element you want to remove duplicates")
#count = 0
for i in range(0,len(l)):
    if l[i] == a:
        count += 1
print(count)
if count >1:
    l.remove(a)
print(l)