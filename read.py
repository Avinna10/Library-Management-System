def read_():
    """This funtion is to read the text file and display details of books in organized way."""
    print("\n\t\t*******************Detail of the Available books*******************\n")
    print("------------------------------------------------------------------------------------------------------")
    print("Book ID\t|\tBook Name\t|\tAuthor\t\t|\tGenre\t|\tStock\t|\tPrice")
    print("------------------------------------------------------------------------------------------------------")
    file = open("book.txt","r")
    bookid = 1
    for line in file:
        #print details of book by removing \n from end and replacing "," by white space
        print("  ",bookid,"\t|\t"+line.strip("\n").replace(",","\t|\t"))
        bookid += 1
        print("------------------------------------------------------------------------------------------------------")
    file.close()

