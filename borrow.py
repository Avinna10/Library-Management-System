#imports datetime module
import datetime

def show():
    """This function allows to read the lines of file and add lines to the list"""  
    file = open("book.txt","r")
    books = []
    for a in file:
        books.append(a.strip("\n").split(","))
    file.close()
    return books

def reduce(list_id):
    """This function reduces the quantity of books after borrowed."""
    book = show()
    change = int(book[list_id][3])
    change = change - 1
    book[list_id][3] = str(change)
    #writing a file after reducing the quantity
    file = open("book.txt","w")
    for a in range(len(book)):
        file.write(str(book[a][0])+","+str(book[a][1])+","+str(book[a][2])+","+str(book[a][3])+","+str(book[a][4])+"\n")
    file.close()        

def total_(name, total):
    """This function adds the total price to the text file."""
    filename = name.upper() + "-Borrow.txt"
    file = open(filename,"a")   
    file.write("\n\t\t\tTotal price of the book: $" + str(total) + "\n")
    file.close()

def borrow_note(name, lname, bookname, price, count, total):
    """This function creates a borrow note with unique name"""
    x = datetime.datetime.now()
    #gives date in year:month:day / hour:minute:second format
    date = x.strftime("%y-%m-%d / %H:%M:%S")    
    filename = name.upper() + "-Borrow.txt"
    #while user borrows single book
    if count == 1:
        file = open(filename,"w")
        file.write("\t\t\t*****Borrower's Detail*****\n\n")
        file.write("Name of the borrower: " + name.upper() + " " + lname.upper() + "\n\n")
        file.write("-----------------------------------------------------------------------------\n")
        file.write("S.N.\t|\tBook Name\t|\tDate and Time\t\t|\tPrice\n")
        file.write("-----------------------------------------------------------------------------\n")
        file.write(str(count)+"\t|\t"+bookname+"\t|\t"+date+"\t|\t"+str(price)+"\n")
        file.write("-----------------------------------------------------------------------------\n")
        file.close()
    #if user wishes to buy multiple books
    elif count>1:
        file = open(filename,"a")
        file.write(str(count)+"\t|\t"+bookname+"\t|\t"+date+"\t|\t"+price+"\n")
        file.write("-----------------------------------------------------------------------------\n")
        file.close()

def full_borrow():
    """This functions asks user to input details and calls the necessary functions to operate."""
    naming_check = True
    while naming_check == True:
        name = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        #It checks whether the input data is alphabets or not
        if name.isalpha() == True and lname.isalpha() == True:
            borrow_loop = True
            total = 0
            count = 0
            borrow_book = []
            ques = True
            show2 = show()

            while borrow_loop == True:
                try:
                    #if id is inputted other than integer except block runs
                    id  = int(input("Enter the ID of book: "))
                                           
                    list_id = id-1
                    #checks if id provided consist in file or not
                    if id < 1 or id > len(show2):
                        print("\nInvalid ID.\n")

                    #checks if book is out of stock or not
                    elif show2[list_id][3] != 0 and int(show2[list_id][3]) > 0:
                        book_approve = True
                        for i in range(len(borrow_book)):
                            #if condition checks if book is borrowed or not
                            if show2[list_id][0] == borrow_book[i][0]:
                                print("\nYou have already borrowed this book.\n")
                                book_approve = False
                                ques = True        

                        while book_approve == True:
                            #adds the detail of the books user chose to list
                            borrow_book.append(show2[list_id])
                            bookname = str(borrow_book[count][0])
                            price = str(borrow_book[count][4])
                            total += int(borrow_book[count][4].replace("$", ""))
                            count += 1

                            #calling function borrow_note to generate text file                   
                            borrow_note(name, lname, bookname, price, count, total)

                            print("\n***Book Borrowed Successfully***\n******Thanks for borrowing******\n")
                            #calling fuction reduce to decrease quantity
                            reduce(list_id)
                            ques = True
                            book_approve = False
                    #if book is out of stock
                    else:
                        print("\nBook is out of stock!!\n")

                    #while loop enables to borrow multiple books until user quits
                    while ques == True:
                        #asks user to borrow multiple books or not
                        ask = input("Do you want to borrow next book? (Yes/No)\n")

                        #if user inputs no book receipt is shown
                        if ask.upper() == "NO":
                            borrow_loop = False
                            ques = False
                            print("\n***Book Borrowed Successfully***\n")
                            print("\t***Borrow Receipt***")
                            print(" -------------------------------")
                            print("| Book Name\t|\tPrice\t|")
                            print(" -------------------------------")
                            for i in range(len(borrow_book)):
                                print("|",borrow_book[i][0],"\t|\t",borrow_book[i][4],"\t|")
                                print(" -------------------------------")
                            print("\n\tTotal price: $",total,"\n")

                        #if inputs yes borrow_loop is run
                        elif ask.upper() == "YES":
                            borrow_loop = True
                            ques = False
                            
                        else:
                            print("\nEnter either yes or no only.\n")
                            ques = True

                except:
                    print("\nID of the book ranges from 1-10.\n")
            #after borrwing is complete it helps to print total price
            if count != 0:
                total_(name, total)
            naming_check = False    #it stops the loop

        else:
            print("\nName should not contain numbers!!!\nEnter only alphabet.\n")
            naming_check = True
