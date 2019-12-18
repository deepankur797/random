x=2
print(x == 2)
print(x == 3)
print(x<3)

#Boolean operators

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# in operator
#The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
mylist=["John","Rick"]

if name in mylist:
    print("You are here with us")

# if else statement block in python
x=3
if(x==2):
    print("x is 2")
elif(x==3):
    print("x is 3")
else:
    print("value doesnot match")

