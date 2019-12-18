# variables in python
myint=7
print(myint)
    #float variable in python
myflaot= float(9)
print(myflaot)
    #strings in python
str1='hello'
str2="hello world"  #this double quote notation helps to declare astrophoe in sentence
str3="Don't fuck it so hard"
print(str1,",",str2,str3)
    #some variation fofr string result
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
    #assignments can be done more than one at a time
a,b=3,4
print(a,b)
    #mixing between no and string is not supported
# print(one+str1)

''' ASSIGNMENT -/-/-/-/-/
The target of this exercise is to create a string, an integer, and a floating point number. 
The string should be named mystring and should contain the word "hello". 
The floating point number should be named myfloat and should contain the number 10.0,
 and the integer should be named myint and should contain the number 20.

mystring = None
myfloat = None
myint = None


if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

'''
print("######################################################")
mystring="hello"
myFloat=float(10)
myInt=20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)