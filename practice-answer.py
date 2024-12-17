# 1. write a program to input 2 numbers & print their sum.

# first = int(input("enter first: "))
# second = int(input("enter second: "))

# print("sum = ", first + second) 

# 2. write a program to input side of a square & print its area.

# side = int(input("enter square side : "))
# print("area = ", side * side)

# 3. write a program to input 2 floating point numbers & print their average. 

# a = float(input("enter first: "))
# b = float(input("enter second: "))

# print("average", (a + b) / 2)

# 4. write a program to input 2 integer number a & b, print True if a is greater than or equal to , if not print false. 

# a = int(input("enter first: "))
# b = int(input("enter second: "))

# print(a >= b)

# 5. write a program to input user first name & print its length.

# str = (input("enter your name : "))
# print(len(str))

# 6. write a program to find the occurance of "$" in a string. 
   
# str = "today i earn 234$ but i was seen previouslly 500$ in my bank"
# print(str.find("$"))

# 7. write a program to take a student mark and place them into a right grade. 

# - above 90 -> grade(A)
# - 80 - 90 -> grade(B)
# - 70 - 80 -> grade(C)
# - 60 - 70 -> grade(D)
# - 50 - 60 -> grade(E)
# - below 50 -> grade(F -> future chaiwala)

# mark = int(input("enter you mark : "))

# if(mark > 90):
#     grade = "A"
# elif(mark >= 80 and mark < 90):
#     grade = "B"
# elif(mark >= 70 and mark < 80):
#     grade = "C"
# elif(mark >= 60 and mark < 70):
#     grade = "D"
# elif(mark >= 50 and mark < 60):
#     grade = "E"
# else:
#     grade = "F - fail"

# print("Grade of the student is -> ", grade)


# 1. write a program to ask the user to enter names of their 3 favorite movie & 
# store them in a list. 

# movies = []
# mov1 = input("enter 1st movie: ")
# mov2 = input("enter 2nd movie: ")
# mov3 = input("enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# 2. write a program if a list contain a palindrome of element. 

# list1 = ["m", "a", "a", "m","p"]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# 3. write a program to count the number of student with "A" grade in the following tuples. 
# ex. ("C","D","A","A","B","B","A") and store the above value in a list & sort them from "A" to "D".

# grade = ["C","D","A","A","B","B","A"]
# print(grade.count("A"))
# grade.sort() 
# by applying sort method you can change tuple to list because tuple 
# object have no any method of sort.
# print(grade)

# python function 

# 1. write a function to print the length of a list(list is a parameter)

# cities = ["delhi", "mumbai", "cheani", "bhubaneswar", "maharastra"]

# def print_len(list):
#     print(len(list))
#     return print_len

# print_len(cities)

# 2. write a function to print the element of a list in a single line 
# (list is a parameter)

# cities = ["delhi", "mumbai", "cheani", "bhubaneswar", "maharastra"]


# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)

# 3. write a function to print the factorial of n. where n is the parameter.

# def cal_fac(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#         print(fact)

# cal_fac(5)

"""
initially , fact = 1
iteration 1: i = 1
fact = 1 * 1 = 1
print : 1

iteration 2: i = 2
fact = 1 * 2 = 2
print: 2

iteration 3: i = 3
fact = 2 * 3 = 6
print: 6

iteration 4: i = 4
fact = 6 * 4 = 24
print: 24

iteration 5: i = 5
fact = 24 * 5 = 120
print: 120
"""

# 4. write a function to convert USD to INR

def convert(usd_val):
    inr_val = usd_val * 84.9
    print(inr_val)

convert(50)