
#
# for i in range(1,11):
#     if(i == 5):
#         break
#
#     print(i)

number = input('Pls enter your number: -')

for i in range(1,11):
    if (int(number) * i == 60):
        break

    print(int(number) *i)