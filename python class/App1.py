#Let us input Age of two persons, match, average age and marital eligibility

#This section is for the first candidate

Name1 = str(input("Candidate 1 Enter your name:"))
Age1 = int(input("Candidate 1 enter your age:"))
print("You are candidate 1. Your name is: " + Name1)
print("and your age is:",Age1,)

#This section is for the second candidate
Name2 = str(input("Candidate 2 Enter your name:"))
Age2 = int(input("Candidate 2 enter your age:"))
print("You are candidate 2. Your name is: " + Name2)
print("and your age is:",Age2,)

#Calculate their average age
Ave = (Age1 + Age2)/2
print("Your average age is", Ave)

#Conditional statement to confirm eligibility
if Ave >=18:
    status= Name1, "And", Name2, "Are eligible for marriage"

else:
    status= "Oooops -- Sorry there is a mismatch", Name1, "And", Name2, "are not eligible to marry"

    #This section prints the marrital Eligibility

print(status)

