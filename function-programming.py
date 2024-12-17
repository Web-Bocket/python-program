# example of function 

# def sum(a,b): # a & b are the parameter
#     sum = a + b
#     print(sum)
#     return sum

# sum(3,4) # 3, 4 are the arguments of that parameter
# sum(4,5)

# ex. print n to 1 backward... 

def show(n):
    if(n == 0): # base case, where our program stop their working
        return
    print(n)
    show(n-1)
show(10)
