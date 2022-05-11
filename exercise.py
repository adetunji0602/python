
#Age prediction app

dob = input("What is your birth year")
Current_year = int(2022)
age = (int(Current_year) - int(dob))
print("your age is: ",age)
 
#Password Checker

Username = input("Enter a username")
Username = str(Username)
Pass = input("Enter your password")
Pass_Length = len(Pass)
Pass_Output = '*' * Pass_Length

print(f'{Username}, Your password is: , {Pass_Output}')
