#import datetime module
import datetime
#import showfunction from borrow module
from borrow import show

def increase(list_id):
    """This function increases the quantity of the book after returned."""
    book = show()
    change = int(book[list_id][3])
    change = change + 1
    book[list_id][3] = str(change)
    #writing book details after increasing quantity
    file = open("book.txt","w")
    for a in range(len(book)):
        file.write(str(book[a][0])+","+str(book[a][1])+","+str(book[a][2])+","+str(book[a][3])+","+str(book[a][4])+"\n")
    file.close()

def return_book(name, lname, books, time, length):
    """This function generates text file containing note of return."""
    x = datetime.datetime.now()
    #gives date in year:month:day / hour:minute:second format
    date = x.strftime("%y-%m-%d / %H:%M:%S")
    totalprice = 0
    book_no = 0
    shows = show()
    booklist = []
    filename = name.upper() + "-Return.txt"
    file = open(filename,"w")
    file.write("\t\t\t*****Return Detail*****\n\n")
    file.write("Name of the returner: " + name.upper() + " " + lname.upper() + "\n\n")
    file.write("-----------------------------------------------------------------------------\n")
    file.write("S.N.\t|\tBook Name\t|\tDate and Time\t\t|\tPrice\n")
    file.write("-----------------------------------------------------------------------------\n")
    #details of returned book(name, date and price) is written to text file
    for j in range(len(books)):
        serial_no = j+1
        file.write(str(serial_no)+"\t|\t"+books[j][2]+"\t|\t"+date+"\t|\t"+books[j][6]+"\n")
        file.write("-----------------------------------------------------------------------------\n")
        totalprice = totalprice + int(books[j][6].replace("$",""))
        book_no += 1
        booklist.append(books[j][2])    #adding bookname to list
        booklist.append(books[j][6])    #adding price to list
    for a in range(len(booklist)):
        for b in range(len(shows)):
            #checks if bookname consist in the index b or not
            if shows[b][0] == booklist[a]:
                list_id = b
                #calling increase function
                increase(list_id)
    file.write("\n\tPrice of the book: $"+ str(totalprice)+"\n")
    file.write("\tLend Duration:\t"+str(time)+"days\n")
    file.write("\tLate Submission Fine:\t$"+str(length*1.75*book_no)+"\n\n")
    file.write("\tTotal price to be paid: $"+str(length*1.75*book_no+totalprice))
    file.close()
    #prinitng receipt in the shell
    print("\n***Book Returned Successfully***\n")
    print("\t***Return Receipt***")
    print(" -------------------------------")
    print("| Book Name\t|\tPrice\t|")
    print(" -------------------------------")
    for i in range(0,len(booklist),2):
        print("|",booklist[i],"\t|\t",booklist[i+1],"\t|")
        print(" -------------------------------")
    print("\nLate Submission Fine:\t$"+str(length*1.75*book_no))
    print("Total price to be paid: $",length*1.75*book_no+totalprice,"\n")
    
        
def return_back():
    """This functions asks user to input details and calls the necessary functions to operate.
    It also makes sure that user have borrowed the book earlier so he/she can return."""
    naming_check = True
    while naming_check == True:
        name = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        #It checks whether the input data is alphabets or not
        if name.isalpha() == True and lname.isalpha() == True:
            filename = name.upper() + "-Borrow.txt"
            
            try:
                books = []
                borrow_details = []
                #if file named filename does not exist it gives error which is handled by execute block
                file = open(filename,"r")
                for a in file:
                    borrow_details.append(a)
                file.close()
                
                try:
                    #if id is inputted other than integer except block runs
                    time = int(input("Enter the duration of borrowed (in days): "))
                    #checks if inputted time is less than 1 or not
                    if time <= 0:
                        print("\nEnter the valid duration.\n")
                    else:
                        length = time - 10
                        if length <= 0:
                            length = 0
                        #add details of borrowed books to the list books
                        for i in range(7,len(borrow_details)-2,2):
                            books.append(borrow_details[i].strip("\n").split("\t"))
                        #calling function return_book
                        return_book(name, lname, books, time, length)
                         
                except:
                    print("\nEnter the duration in numeral system.\n")
                naming_check = False    #it ends the while loop
            except:
                print("\n",name.upper(),", You have not borrowed book yet.\n")
                naming_check = False    #it ends the while loop
            
        else:
            print("\nName should not contain numbers!!!\nEnter alphabet only.\n")
            naming_check = True     #works on loop until user inputs name correctly.
