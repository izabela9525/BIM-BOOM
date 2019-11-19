# Class can use functions, constancts, constructors, variables

# First we are creating a class
class A:
    # This is clas function
    def funcName(self):
        print("This is class function")

# To call any member of class, create object of that class
object = A()

# Call functions of class by using object
object.funcName()