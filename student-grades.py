print('Welcome to Cool School App. What would you like to do?'),
print('1. Add Student'),
print('2. Add Student Grade'),
print('3. Get Student Avg'),
print('4. Remove Student'),
print('5. End Program')

student_records = [] #empty list to be filled with dictionarys of students and records.

def enter_task():
    
    #return "hi"
    
    task = input('Input Task Number:')

    return recieve_task(task)

def recieve_task(task):
       
    if (task == "1"):
        #enter new students name: for input into records
        user_input = input('Enter new students name:'), 1 #: (user input, input type)
        
    if (task == "2"):
        #enter students name: for grade
        user_input = input('Enter students name:'), 2 #: (user input, input type)
        
    if (task == "3"):
        #enter new students name: to get student avg grade 
        user_input = input('Enter students name:'), 3 #: (user input, input type)
        
    if (task == "4"):
        #enter new students name: to remove student
        user_input = input('Enter students name:'), 4 #: (user input, input type)
    
    if (task == "5"):
        print ("Thanks for using Cool School App. Bye")
    else:
        do_something(user_input)
        
def do_something(recieved):
    
    if (recieved[1] == 1):
        new_record = {'name': recieved[0], 'grades':[]}
        student_records.append(new_record)
    
    if (recieved[1] == 2):
        grade = input('Enter the student\'s grade. (Numbers 0-100 only)')
        grade = int(grade)
        for i in student_records:
            if(i['name'] == recieved[0]):
                i['grades'].append(grade)
    
    if (recieved[1] == 3):
        num = False
        k = 0
        for i in student_records:
            if(i['name'] == recieved[0]):
                num = len(i['grades'])
                if(num > 0):
                    avg = sum(i['grades'])/num
            
        if(num != False):
            if(num > 0):
                print("The averge grade for {}\'s {} was {}".format(recieved[0], num, avg))
            else:
                print("Looks like {} does not have any grades entered".format(recieved[0]))
        else:
            print("No record of a student with the name \'{}\' was found".format(recieved[0]))
        

    if (recieved[1] == 4):
        remove = False
        k = 0
        for i in student_records:
            if(i['name'] == recieved[0]):
                remove = True
                index = k
            k +=1
        if(remove != False):
            del student_records[index]
            print("{} was removed from the student records".format(recieved[0]))
        else:
            print("No record of a student with the name \'{}\' was found.".format(recieved[0]))
    
    enter_task() # run it again
           
enter_task()

