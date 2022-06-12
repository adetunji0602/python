

# def ade():
#     Name = input(str('Enter your name: '))
#     Age = input('Enter your age: ')
#     print (Name, 'is', Age)

# ade()

# x = 1921
# print(type(x))
# STR = str(x)
# print(STR)
# print(type(STR))

# def sum(num1, num2):
#     return num1 + num2
#     # greeting = "hello"
# print(f'The sum of the two number is {(sum(10,5))}')

# def sum(num1, num2):
#      return num1 + num2
# total = sum(10,5)

# print(sum(10,total))


def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)


total = sum(10,5)
print(total)