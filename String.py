# # str1 = ("this is a string. \n We are creating it in python")
# # print(str1)
# # print(len(str1) )  # Length of the string

# # str2 = "Hello"
# # str3 = 'World'
# # str = str2 + " " + str3
# # print(str)

# # print(len(str2))  # Length of str2
# # print(len(str3))  # Length of str3
# # print(len(str))  # Length of the concatenated string

# str = "Hello, World!"
# print(str[0])      # H
# print(str[7])      # W

# print(str[1:4])   # ell
# print(str[:5])   # 0 : 5 
# print(str[7:])   # 7 : len(str)
# print(str[-1])    # !  # Last character
# print(str[-5:-2])  # orl

str = " i am studying python programming "
print(str.endswith("ing "))  # True
print(str.endswith("pro"))  # False
print(str.count("i"))  # 3
print(str.capitalize())  # I am studying python programming
print(str.find("python"))  # 15
print(str.find("Q"))  # -1
print(str.replace("python", "Java"))  # i am studying Java programming
print(str.strip())  # "i am studying python programming"
print(str.upper())  #  I AM STUDYING PYTHON PROGRAMMING
print(str.lower())  #  i am studying python programming