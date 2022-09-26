class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        lenddict = {}

    def displaybook(self):
        print("we have following in our library:" +self.name)
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.update({book:user})
            print("Lender book has been updated.you can take the book")
        else:
            print("book is already used by" + self.lenddict[book])

    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added in booklist")


    def returnbook(self,book):
        self.booklist.remove(book)

if __name__ == "__main__":
    vikram = library(['python','C++','Java'])

    while(True):
        print("welcome to" + vikram.name + "library. Enter your choice to countinue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3.Add a Book")
        print("4. Return a Book")
        user_choice = int(input())
        
        if user_choice == 1:
            vikram.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of book you want to lend")
            user = input("Enter your name")
            vikram.lendbook(user,book)



        elif user_choice == 3:
            book = input("Enter the name of the book in add")
            vikram.addbook()

        elif user_choice == 4:
            book = input("Enter the name of the book in Return")
            vikram.returnbook()
            
        else:
            print("Not a valid option")    
            
        print("Press q to quit and c to countinue")
        user_choice = input()
        if user_choice == "q":
            exit
        if user_choice == "c":
            continue
