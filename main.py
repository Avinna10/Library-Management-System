#importing modules read, borrow and returnback
import read
import borrow
import returnback

loop = True
round = True

#welcome message
print("\n\t\t*******************************************************************")
print("\t\t****************************  WELCOME  ****************************")
print("\t\t*******************************  TO  ******************************")
print("\t\t*******************  LIBRARY MANAGEMENT SYSTEM  *******************")
print("\t\t*******************************************************************\n")

    
while loop == True:
    #asks user to use the system or exit
    continuity = input("Do you want to enter the system? (Yes/No) \n")

    while round == True:
        #if user inputs yes
        if continuity.upper() == "YES":
            print("1. View Books\n2. Borrow Books\n3. Return Books\n4. Exit\n")

            """try block runs if input given is integer.
            If input is any other than integer except block is runs"""
            try:                     
                option = int(input("Choose an option from above list--> "))

                #if user inputs 1
                if option == 1:
                    read.read_()    #calls the function read_ of read module

                #if user inputs 2
                elif option == 2:
                    borrow.full_borrow()    #calls the function full_borrow of borrow module                          

                #if user inputs 3        
                elif option == 3:
                    returnback.return_back()    #calls the function return_back of returnback module

                #if user inputs 4
                elif option == 4:
                    print("\n\t\tThanks for using library management system!!!\n")
                    round = False
                    loop = False

                else:
                    print("Invalid Option!!\n")
            except:
                print("Numeric value is only accepted!!!\n")

        #if user inputs no
        elif continuity.upper() == "NO":
            print("Thanks for visiting!!")
            loop = False
            break

        #if user inputs anything excpet yes/no
        else:
            print("Enter either yes or no only.\n")
            break
