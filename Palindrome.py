# list = ("madam",12321,"racecar",45654,"hello",78987)

# for item in list:
#     if str(item) == str(item)[::-1]:
#         print(f"{item} is a palindrome")
#     else:
#         print(f"{item} is not a palindrome")

list = [1,2,3,3,2,1]

list_copy = list.copy()
list_copy.reverse()
if (list_copy == list):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")