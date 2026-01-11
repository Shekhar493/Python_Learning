n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
n3 = input("Enter third number: ")

if (n1 >= n2) and (n1 >= n3):
    print("Greatest number is:", n1)
elif (n2 >= n3):
    print("Greatest number is:", n2)
else:
    print("Greatest number is:", n3)

