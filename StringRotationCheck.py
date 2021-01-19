str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("String not rotation of each other")
str1 += str1
if str1.count(str2) > 0:
    print("Strings are rotation of each other")
