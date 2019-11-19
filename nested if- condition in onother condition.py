#nested if- it's mean that the condition in onother condition

#Take one number from the user

num = input("Please enter your number ")
num = int(num)

if(num >= 0):
    if(num %2 == 0):
        print("This is even number")
    else:
        ("This is odd number")
else:
    print("This is negeative number")