tuple1 = (45,'Testing', "www.thetestingworld.com", 23.4, "Yes", "No")
tuple2 = (100, 200)

# Count number of times a value displayed in Tuple
# 1print(tuple1.count(45))

# Find index of any value in tuple
# print(tuple1.index(23.4))

tuple3 = tuple1 + tuple2
print(tuple3)

for i in tuple1:
    print(i)


i = len(tuple1)
for i in range(0,1):
    print(tuple1[i])