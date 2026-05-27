#Create a list of the book with title and Author
#The book is available or not.
#When will book be returned.
#Library Book Tracker - Project Requirements





#Class namespace called Book has been created

class Book():
    '''Attributes and Methods are describe below'''
    def __init__(self, title, author):
        self.title=title # Attributes
        self.author=author# Attributes
        self.borrowed=False # Attributes sets at False
        
    def rented(self): #Method
        if self.borrowed==True:
            print("Already borrowed")
        else:
            self.borrowed=True
            print("Not available")
                    
    def returned(self): # Method
        if self.borrowed==True:
            self.borrowed=False
            print("Book returned")
        else:
            
            print("Wasn't borrowed")       
            
    def show_info(self):# Method
        if self.borrowed == True:
            print(self.title, self.author,": Borrowed") 
        else:
            print(self.title, self.author,": Available")    
 
     
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Hobbit", "J.R.R. Tolkien")
book5 = Book("Pride and Prejudice", "Jane Austen")
book6 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book7 = Book("The Catcher in the Rye", "J.D. Salinger")
book8 = Book("The Lord of the Rings", "J.R.R. Tolkien")
book9 = Book("Animal Farm", "George Orwell")
book10 =Book("Brave New World", "Aldous Huxley")
    
    
book1.rented()

book1.show_info()    
    
book1.returned()   

book1.show_info()