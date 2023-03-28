#Stage 1
#Initializing an empty list and vars
students = []
option = ""
name= ""
courses = ""
remove = ""

print("###########################")
print("Hi!, welcome to this app :)")

#Executing the code infinitely
while True: 
    #Charging the options
    print("###########################")
    print("Enter the number you want to run: ")
    print("1 - See the list of students")
    print("2 - Add a new student to the list")
    print("3 - Remove student from the list")
    print("4 - Exit")
    option = input("-->")
    print("###########################")
#Option to show the list
    if option == "1":
        if students != []:
            print("List of students:")
            for i in range(len(students)):
                name = students[i][0]
                courses = students [i][1]
                str(courses)
                print(name, " - ", courses, " courses")
                i = i + 1
        else:
            print("This list is empty!")
#Option to charge students to the list
    elif option == "2":
        print("Please, enter the student´s name: ")
        name = input("-->")
        print("Now, enter the number of courses: ")
        courses = input("-->")
        if name == "" or courses == "":
            print("Error!, the information was incorrectly loaded, please, try it again.")
        else:
            students.append([name, courses])
            print("The information was correctly loaded.")
#Option to remove students
    elif option == "3":
        print("Choose the line you want to delete:")
        for i in range(len(students)):
            name = students[i][0]
            courses = students [i][1]
            str(courses)
            print(i + 1, name, " - ", courses, " courses")
            i = i + 1            
        remove = int(input("-->"))
        remove = remove - 1 
        if remove <= len(students) and remove != -1:
            del students[remove]
            print("The student was removed correctly")
        else:
            print("That number is not valid.")
#Option to finish the program
    elif option == "4":
        break
    else:
        print("The entered option is not valid.")

print("Thanks for using this app! :)")
print("###########################")


