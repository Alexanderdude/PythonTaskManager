   
bStop = True


while bStop == True :  # Starts a loop
        
    Username = input("\n" + "Please enter your username : ")  # Asks for a username from the user
    
    U = open('user.txt','r+')  # Opens file
            
    for line in U : # Checks each line of code
            
        sLogin = line

        iFound = sLogin.find(",")  # Looks for the comma

        sName = sLogin[0:iFound]  # Gets the username from the file

        if sName == Username :  # Does the username match

            print("\n")
            
            Password = input("Please enter your password : ")  # Gets the password from the user
            
            Pass = sLogin[iFound + 2:len(sLogin) - 1]  # Gets the password from the file
            
            if Pass == Password :  # Do they match
        
                bStop = False # stops the loop 

                break  # Stops the loop

                print("there")

                U.close()

            else :

                print("\n" + "Error. Invalid password entered.")  # Error message

            
    if sName != Username :  

        print("\n" + "Error. Invaid username entered")  # Error message






sStop = True

while sStop == True :
    
    print("\n" + "Please select one of the following options:")  # login info

    print("r - register user" + "\n" + "a - add task" + "\n"
          + "va - view all tasks" + "\n" + "vm - view my tasks" + "\n" + "e - exit")

    if sName == "admin" :

        print("s - statistics")

    sChoice = input("\n" + "What is your choice : ")  # Gets the users choice





    if (sChoice == "r") and (sName == "admin") : # Did you user click 'r'

        Newname = input("\n" + "Please enter a new username : ")  # Gets variables from the user

        NewPass = input("\n" + "Please enter a new password : ")

        confpass = input("\n" +"Please confirm your password : ")

        U = open("user.txt","r+")

        if confpass == NewPass :  # Do the 2 passwords match

            U.write("\n" + Newname + ", " + confpass + " ")  # adds to the file

            U.close()

        else :

            print("\n" + "The passwords dont match!")  # Error message





    if (sChoice == "r") and (sName != "admin") :  # Checks if the user is allowed to add a new user

        print("\n" + "You are not permited to add a new user!") # Error message





    if sChoice == "e" :  # exits the loop

        sStop == False

        break





    if sChoice == "a" :

        T = open("tasks.txt","a") # opens file
        
        Username = input("\n" + "Please enter the username of the person the task is assigned to : ")  # assigns variables

        Title = input("\n" + "What is the title of the task : ")

        Desc = input("\n" + "What is the description of the task : ")

        DueDa = input("\n" + "What is the start date of this task: ")

        DueDate = input("\n" + "What is the end date of this task: ")

        Fulla = Username + ", " + Title + ", " + Desc + ", " + DueDa + ", " + DueDate + ", " +"No"  # concatenates a string

        T.write(Fulla + "\n")  # writes the string to the file

        T.close()
        




    if sChoice == "va" :

        list = ["Username : ","Title : ","Description : ","Due Date : ","Task Completed : "]  # creates a list

        T = open("tasks.txt","r+")

        for line in T :

            sTask = line

            print("\n" +"\n" + "TASK:")

            for i in range(0,5) :  # starts a loop

                if i == 3 :

                    iFound = sTask.find(",")  # Finds the comma

                    string = sTask[0:iFound]  # gets everything before the comma

                    sTask = sTask[iFound + 2:len(sTask)]  # Removes the comma and everything before

                    iFound = sTask.find(",")

                    string = string + " - " + sTask[0:iFound]

                    print("\n" + list[i] + string)  # Displays the output

                    sTask = sTask[iFound + 2:len(sTask)]

                else :
                    
                    iFound = sTask.find(",")

                    string = sTask[0:iFound]

                    print("\n" + list[i] + string)  # displays the output

                    sTask = sTask[iFound + 2:len(sTask)]
        T.close()






    if sChoice == "vm" :

        list = ["Username : ","Title : ","Description : ","Due Date : ","Task Completed : "]  # creates a list

        T = open("tasks.txt","r+")

        for line in T :

            sTask = line

            iFound = sTask.find(",")  #finds the comma

            string = sTask[0:iFound]  # gets everything before the comma
            
            if string == sName :  # checks if the user signed in has any tasks in the file
                
                print("\n" +"\n" + "TASK:")

                for i in range(0,5) :

                    if i == 3 :

                        iFound = sTask.find(",")  # finds the comma

                        string = sTask[0:iFound]  # Gets everything before the comma

                        sTask = sTask[iFound + 2:len(sTask)]  # removes the previously used string

                        iFound = sTask.find(",")  # redo

                        string = string + " - " + sTask[0:iFound]

                        print("\n" + list[i] + string)  # displays the output
   
                        sTask = sTask[iFound + 2:len(sTask)]

                    else :
                    
                        iFound = sTask.find(",")

                        string = sTask[0:iFound]

                        print("\n" + list[i] + string)

                        sTask = sTask[iFound + 2:len(sTask)]

        T.close()





    if (sChoice == "s") and (sName == "admin") :  # Checks if the user is an admin and selected "s"

        T = open("tasks.txt","r+") # opens files

        U = open("user.txt","r+")

        icount = 0 

        for lines in T :  # in each line

            icount+=1  # counts the number of line

        print("\n\n" + "The total number of tasks are : " + str(icount))  # displays output

        icount = 0

        i=0

        for lines in U : # counts the lines in the file

            i += 1

            if (i % 2)  == 0 :  # counts every second line
                
                icount += 1 
                
        icount = icount + 1  # adds 1 more to the icount

        print("\n" + "The total number of users are : " + str(icount))  # displays output

        T.close()  # close the file

        U.close()

        
 
    


print("\n" + "You have signed out!")  # message

