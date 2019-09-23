Cool School App

A simple Python application to store student names and their grades.

Start:

Print list of application instructions:
    1. Add Student
    2. Add Student Grade
    3. Get Student Avg
    4. Remove Student
    5. End Program

define "enter_task" function
    input prompt for task number
    
    coditonal statemtents checking for users input (1-5)
    
    if 1:
        input prompt for student name
        take the users input name and put into a student records list (list of dictionarys with name, and grades list).
        go to bottom of function 
    if 2:
        input prompt for student name
        take the users input name and find in student records list.
        input prompt for students grade
        place grade into grade list inside the dictionary
        go to the bottom of the function
    if 3.
        input prompt for student name
        take the users input name and find in student records list.
        grab the list of grades for the student. Find the number of grades then calculate the avg.
        print the grade avg.
        go to the bottom of the function
    if 4.
        input prompt for student name
        take the users input name and find in student records list.
        delete the index with the record matching the students name.
        go to the bottom of the function
    if 5.
        end prorgram. print thank you message.
    else
        call "enter_task" functiot to run the program again

initial call for the "enter_task" function 
        
