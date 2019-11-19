num = input("Please enter your age --> ")
num = int(num)

if (num < 0):
    print("its a negative number")
elif (num == 0):
    print("zero")
elif (num %2 == 0):
    print("liczba parzysta")
else:
    print("this is odd number, nieparzysta, nieujemna, nie 0")