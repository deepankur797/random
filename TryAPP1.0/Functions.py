'''
FUNCTIONS IN PYTHON

Functions are convenient way to divide your code into useful blocks, all that blah-blah
'''

# writting function in python
# It uses block statements concept
#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
# For example:

def my_function():
    print("My first function")

#Functions may also receive arguments (variables passed from the caller to the function). For example:
def my_func_args(username,greetings):
    print("Hello %s,From My Function!, I wish you %s" %(username,greetings))
#return statement
def sum(a,b):
    return a+b

#Calling functions with this thing
my_function()
my_func_args("DS","A Happy New Year")
x=sum(1,2)
print(x)

