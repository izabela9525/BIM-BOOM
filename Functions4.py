# print("Reguired Arguments - if I define two arguments I want two arguments in calling the function")
def takeInput(a, b):
    c = a + b
    print("Sum of Values " + str(c))


takeInput(10, 52)


# print("Keyword Arguments - when I calling the function I named my arguments")
def takeMyInput(a, b):
    c = a + b
    print("Sum of Values " + str(c))


takeMyInput(b=100, a=500)


# print("Default Arguments - I can define one of the arguments
# and when I calling function I can named one arg")

def takeDefArgument(a, b = 10):
    c = a + b
    print(c)


takeDefArgument(a = 120)