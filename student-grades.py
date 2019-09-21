#David, Utsav, Daniel, Greg
#v2

print('Welcome to Cool School App. What would you like to do?'),
print('1. Add Student'),
print('2. Add Student Grade'),
print('3. Get Student Avg'),
print('4. Remove Student'),
print('5. End Program')

student_records = [] #empty list to be filled with dictionarys of students and records.

def enter_task():
    
    name_input = "Enter students name:"
    
    task = input('Input Task Number:')
    if (task == "1"):
        #enter new students name: for input into records
        user_input = input('Enter new students name:')

        new_record = {'name': user_input, 'grades':[]}
        student_records.append(new_record)
        
    if (task == "2"):
        #enter students name: for grade
        user_input = input(name_input)
        grade = input('Enter the student\'s grade. (Numbers 0-100 only)')
        grade = int(grade)
        for i in student_records:
            if(i['name'] == user_input):
                i['grades'].append(grade)
        
    if (task == "3"):
        #enter new students name: to get student avg grade 
        user_input = input(name_input)
        num = False
        k = 0
        for i in student_records:
            if(i['name'] == user_input):
                num = len(i['grades'])
                if(num > 0):
                    avg = sum(i['grades'])/num
            
        if(num != False):
            if(num > 0):
                print("The averge grade for {}\'s {} grade(s) is {}".format(user_input, num, avg))
            else:
                print("Looks like {} does not have any grades entered".format(user_input))
        else:
            print("No record of a student with the name \'{}\' was found".format(user_input))
        
    if (task == "4"):
        #enter new students name: to remove student
        user_input = input(name_input)
        remove = False
        k = 0
        for i in student_records:
            if(i['name'] == user_input):
                remove = True
                index = k
            k +=1
        if(remove != False):
            del student_records[index]
            print("{} was removed from the student records".format(user_input))
        else:
            print("No record of a student with the name \'{}\' was found.".format(user_input))
    
    if (task == "5"):
        print ("Thanks for using Cool School App. Bye")
    else:
        enter_task() # run it again

        
enter_task() #### initial run


