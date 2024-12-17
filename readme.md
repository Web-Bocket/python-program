What is python :- 

- python is simple, easy & portable. 
- python is free & open source. 
- python is high level, interpreted programming language. 
- python was developed by Guido van Rosum. 
- python is interpreted language means when we write python code its executed the code line by line thats why we called python is a interpreted language.. 
- we use ".py" as the exetention of python file. 
- print is a function to give output statement in python, simply we can say "print" is a output function. 

Charter set of python language :- 

1. Letter -> A-Z & a-z
2. Digits -> 0-9
3. Special Character -> -,+,*,/
4. white space -> blank space, tab, new line etc.. 

What is variable in python :- 

- variable is a container to store some data inside it. 
- ex. name = "sanjib", age = 23, salary = 23000
- in the given example name, age, salary is your variable name & sanjib, 23, 23000 is you variable value. 

Rules for Identifiers :- 

1. Identifire -> name of the variable. 
2. identifier can be combination of uppercase & lowercase letter, digits or an underscore(_). 
ex. myVariable, variable_1
3. An identifiers can not start with digit. so while "variable1" is valid but "1variable" is not valid. 
4. we can not use special chaarter or symbols like !,#,@,% etc...
5. identifier can be of any length.
6. variable name should be small & meaningful like - when we give our age in that case we take the variable as "myAge", when we give our name in that case we take the variable as "myName". 



Data Types in Python :- 

- data type means, which type of data we use to give our variable value.
- mainlly datatypes are of 5 types in python. 
- we used "type" operator to know that what type of data we used. 

1. integer -> +ve value, 0, -ve value
2. String -> "hello", "sanjib" etc...
3. Float -> 3.91, 4.00, 9.1 etc...
4. Boolean -> True, False
5. None - not assign.. 

comments in python :- 

- when we write some code but we dont want to execute it then we give the comment line to that place so that line of code will not executed. 
- basically comments are of 2 types..
1. single line commnet - when we give the single line comment in python we did it on "#". 
- ex. #single line comment

2. Multi line comment - when we give the multi line comment in python we did it on """multi line comment""". 

Operator in Python :- 

- Operator means who can operate the operands. simply we can say operator is a symbol that perform a certain operation between operands.
- ex. a + b (a & b are the operands & "+" symbol is our operator)
- there are 4 types of operator are present in python

1. Arithmetic operator -> (+,-,/,*,%,**)
2. Relational Operator -> (==, !=, > , <, >=, <=)
3. Assignment IOperator -> (=, +=, -=, *=, /=, %=, **=)
4. Logical Operator -> (And, or, not)

user input in python :- 

- input() statement is used to accept values(use keyboard) from user.

practice task :-

1. write a program to input 2 numbers & print their sum.
2. write a program to input side of a square & print its area.
3. write a program to input 2 floating point numbers & print their average. 
4. write a program to input 2 integer number a & b, print True if a is greater than or equal to , if not print false. 

String :- 

- string is a datatype that store a sequence of character. 
- ex.
str1 = "this is a good day"
str2 = 'this is a good day'
str3 = """this is a good day"""

- all these strings are real string because in python it supports all of these syntax like - "", '', """ """
- (new line - \n) -> when we want to break our line into a new line then we can give the new line symbol in that place so the line get breaked.

Basic operation of string :- 
1. concatenation -> "hello" + "world" -> "helloworld"
2. Length of string -> len(str)

Indexing of String :-
- Always indexing start from "0"
- ex. webbocket -> 012345678 (indexing)

Slicing of String :- 
- accessing parts of a string.
- ending index is not count.
- syntax -> str[starting_index : ending_index]
ex. 
str = "webbocket"
       0123
str[0:3] -> web
str[4:6] -> oc
str[3] -> bocket
str[:5] -> webbo

Function of String :- 

- ex. str = "i am a coder & i am do coding"
1. str.endswith("g") -> retuns true if string ends with substring.
2. str.capitalize() - returns 1st character in capital
3. str.upper() - returns all character in capital letter
4. str.lower() - return all character in lower letter
5. str.replace("am", "was") - replace old with new 
6. str.find("am") - returns 1st occurance of our string
7. str.count("am") - counts all occurance of substring in string. 

Practice Task :- 5 min

1. write a program to input user first name & print its length.
2. write a program to find the occurance of "$" in a string. 
   str = "today i earn 234$ but i was seen previouslly 500$ in my bank".

Conditional Statement :- 

- it is used to handle the condition in your program.
- syntax :- (if-elif-else)
- elif means "else-if".

if(condition):
    statement1
    elif(condition):
    statement2
    elif(condition):
    statement3
else: 
    statement(default)

Practice Task :- '

1. write a program to take a student mark and place them into a right grade. 

- above 90 -> grade(A)
- 80 - 90 -> grade(B)
- 70 - 80 -> grade(C)
- 60 - 70 -> grade(D)
- 50 - 60 -> grade(E)
- below 50 -> grade(F -> future chaiwala)

2. Write a program to check if a number entered by the user is odd or even
2. write a program to find the greatest of 3 numbers entered by the user
4. write a program to check if a number is a multiple of 7 or not. 

List in Python :- 

- list is a build in data type that stores set of values. 
- it can store elements of different types like integer, string & float etc.. 
- in list we can make indexing. 
- in list we can find length of the list also. 
- in list we can also do the slicing activity. 

ex. 
marks = [45,78,89,94,53,95] - array list - type 1
student = ["web", 67, "bhubaneswar", 56.89] - list - type 2

slicing in list :- 

- it similar to string slicing.
- syntax :- list_name[starting_idx : ending_idx]
- ending index is not count. 
ex. 
marks = [45,78,89,94,53,95]
marks[1:4] -> [78,89,94]
marks[4:5] -> [53]
marks[2:] -> [89,94,53,95]
marks[:5] -> [45,78,89,94,53]

List Methods :-

- list have some method like..
1. list.append() -> adds an element at the end of the list
2. list.sort() -> sort the element in assending order. 
3. list.sort(reverse=True) -> sort the element in decending order
4. list.reverse() - reversing the list
5. list.insert(idx, el) - insert the element in proper index
6. list.remove() - it remove 1st occurance of element
7. list.pop(idx) - remove element at proper index 

Tuple in Python :- 

- Tuple is also a build in data type that lets us create immutable (the value can't be changeble) sequence of values. 
- ex. tup = (34,67,89,90,43)
- tuple also have indexing. 
ex. 
1. tup1 = () -> empty tuple
2. tup2 = (1,) -> tuple
3. tup3 = (67,89,90) -> tuple
- tuple have also satisfying the slicing propertry. 

Tuple Methods :- 
1. tup.index(element) - return index of first occurance.
2. tup.count(element) - return the count of total occurance.

Practice Task :- 

1. write a program to ask the user to enter names of their 3 favorite movie & store them in a list. 
2. write a program if a list contain a palindrome of element. 
3. write a program to count the number of student with "A" grade in the following tuples. 
ex. ("C","D","A","A","B","B","A") and store the above value in a list & sort them from "A" to "D".

Dictionary in Python :- 

- dictionary are used to store the data values in "key:value" pair.
- they are unordered, mutable (changeble) & don't allow duplicate keys. 
- ex. 
dict = {
    "name" : "shradha",
    "CGPA" : 8.9,
    "marks" : [98,78,90]
}
- the left part of the dictionary are the keys & right part of the dictionary are the 
value of that key. 

Nested Dictionary in Python :- 

- Dictionary also satisfy the nested property.
- Dictionary under dictionary is called nested dictionary.
- ex. 
student = {
    "name": "mithun",
    "score": {
        "chem" : 98,
        "math" : 89,
        "phy" : 79
    }
}

Dictionary methods in python :- 

1. myDict.keys() - it returns all keys
2. myDict.values() - it returns all values
3. myDict.items() - it will returns all key:value pair as tuple.
4. myDict.get("key") - returns the value acording to their key. 
5. myDict.update(newDict) - insert the specified items to the dictionary. 

Set in Python :- 

- set is the collection of the unordered items. 
- Each element in the set must be unique & immutable(can't change).
ex. nums = {1,2,3,4}

Set Method :- 

1. set.add(element) -> adds an element
2. set.remove(element) -> remove an element
3. set.clear() -> clear all element
4. set.pop() -> remove a random value of set.
5. set.union(set2) -> combine both set value and returns a new set.
6. set.intersection(set2) -> combines the common value & returns a new set. 

Loops in Python :- 

- loops are used to repeat instruction.
- in python we have 2 loops -> while loop & for loop.

1. While Loop :- 
syntax -> 

initialize
while condition:
    statement
    incre/decre

Break & Continue :- 

break :- break is used to terminate the loop when encountered.
continue :- terminates execution in the current iteration & continue of the loop with the next iteration. 

2. For Loop :- 

- for loop is used for sequential traversal for traversing list, string, tuple etc..
- syntax :- 
for val in list:
    statement....

Range() in python :- 

- range function returns a sequence of numbers starting from 0 by default, and increments by 1 bt default. and stops before a specified numbers. 
- syntax -> range(start, stop, step)

Function in python :- 

- Function is a block of code/statement that perform a specific task. 
- syntax :- 
# function creation
def func_name(parameter 1, parameter 2):
    // some statement
    return value

# function calling
func_name(arg_1, arg_2)

- Normally function are of 2 types in python :- 
1. Build-in function -> print(), len(), type(), range() etc... 
2. user defined function -> user can develop the function. sum() etc..

Practice Task :- 

1. write a function to print the length of a list(list is a parameter)
2. write a function to print the element of a list in a single line (list is a parameter)
3. write a function to print the factorial of n.
5! = n! * (n-1)!
4. write a function to convert USD to INR

Recursion in python :- 

- when the function calls itself repeatedlly is called recursion and this process is called recurance relation. 














