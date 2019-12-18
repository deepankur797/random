
# CLASSES AND OBJECT

#Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
#A very basic class would look something like this:

class MyClass:
    variable ="Hey Baby"

    def func(self):
        print("This message comes from the class")


#We'll explain why you have to include that "self" as a parameter a little bit later.
# First, to assign the above class(template) to an object you would do the following:


myObjectx=MyClass()  #creating objects for the same

print(myObjectx.variable)

#You can create multiple different objects that are of the same class(have the same variables and functions defined).
#However, each object contains independent copies of the variables defined in the class.
#For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:

myObjecty=MyClass()
myObjecty.variable="whoor soniyo"

print(myObjecty.variable)

# similiarly you can access functions of a class

myObjectx.func()
