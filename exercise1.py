#Build a simple counter

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

my_list2 = [2,3,5,7,8,9,11]
counter = 5
for t in my_list2:
    counter = counter + t
print(counter)

#Range

for number in range(0, 10):
    print(list(range(10)))



#While Loop - while a condition is happening, do something
i = 25
while i < 50:
    print(f'i is less than 50')
    break

#Enumerate - USed to get index counter of an item
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')