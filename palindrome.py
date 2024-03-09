string = input("Enter the string")
j = -1
flag = 0
for char in string:
    if char != string[j]:
        flag = 1
        break
    j = j - 1

print(string + " is : ", end="")
print("Not Palindrome") if flag else print("Palindrome")