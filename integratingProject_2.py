#Stage 2
#Functions
def verify(data):
    while data == "":
        print("Error!, loaded empty data")
        print("Please, enter the information again: ")
        data = input("-->")
    return data

def converter(value):
    while value.isdecimal() == False:
        print("Error!, loaded wrong data")
        print("Please, enter a number again: ")
        value = input("-->")
    return value

#Initializing an empty dictionary
students = {}

print("###########################")
print("Hi!, welcome to this app :)")

#Executing the code infinitely
while True: 
#Charging the options
    print("###########################")
    print("Enter the number you want to run: ")
    print("1 - Consult the list of students")
    print("2 - Add a new student to the list")
    print("3 - Remove a student from the list")
    print("4 - Consult a student's courses")
    print("5 - Exit")
    option = input("-->")
    print("###########################")
#Option to show the list
    if option == "1":
        if students != {}:
            print("List of students:")
            for name, courses in students.items():
                print("*", name, " has ", courses, " courses")
        else:
            print("This list is empty!")
#Option to charge students to the list
    elif option == "2":
        print("Please, enter the student´s name: ")
        name = input("-->")
        name = verify(name)
        print("Now, enter the number of courses: ")
        courses = input("-->")
        courses = converter(courses)
        students[name] = courses
        print("The student´s data was correctly loaded")
#Option to remove students
    elif option == "3":
        print("Enter the name you want to delete: ")
        name = input("--> ")
        if name in students:
            del students[name]
            print(name , " was correctly deleted.")
        else:
            print("The name doesn't correspond to a student on the list.")
#Option to consult a stundent's courses
    elif option == "4":
        print("Enter the student's name you wanto to consult:")
        name = input("--> ")
        if name in students:
            print(name, " has ", courses, " courses.")
        else:
            print("The name doesn't correspond to a student on the list.")
#Option to finish the program
    elif option == "5":
        break
    else:
        print("The entered option is not valid.")
print("Thanks for using this app! :)")
print("###########################")


