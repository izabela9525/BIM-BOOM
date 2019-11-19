class A:
    def __init__(self, a, b):
        print("This is constructor")
        c = a + b
        print(c)

    # Function with no argument and no return value
    def hello(self):
        print("Hello")


    # Function, which will take 2 argument, sum value and display
    def sum(self, a, b):
        c = a + b
        print("Sum is - " + str(c))

    # Function which will take argument and return value as well
    def mul(self, a, b):
        c = a * b
        print("Multiply is - " + str(c))
        return c

object = A(2, 5)
object.mul(23,11)