#Michael Webb
#Case Study if...else and while
#This program will prompt the user to enter student names and GPAs
#It will then determine if the student made the Dean's List, Honor Roll, or neither
studentLastName = ""
while studentLastName != "ZZZ":

    studentLastName = input("Enter your last name or ZZZ to quit: ")
    if studentLastName == "ZZZ":
        break
    studentFirstName = input("Enter your first name: ")
    GPA = float(input("Enter your GPA: "))
    if GPA >= 3.5:
        print(f"{studentFirstName} {studentLastName} has made the Dean's List!")
    elif GPA >= 3.25:
        print(f"{studentFirstName} {studentLastName} has made the Honor Roll!")
    else:
        print(f"{studentFirstName} {studentLastName} GPA of {GPA} was not high enough to make the Dean's List or Honor Roll.")
print ("Goodbye!")