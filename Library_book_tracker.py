#Create a list of the book with title and Author
#The book is available or not.
#When will book be returned.
#Library Book Tracker - Project Requirements







class Book():
    '''Attributes and Methods are describe below'''
    def __init__(self, title, author):
        self.title=title # Attributes
        self.author=author# Attributes
        self.borrowed=False
        
    def borrow(self):
        if self.borrowed == True:
            print("Already borrowed")
        else:
            print("Book is available")
                   
    def returned(self):
        if self.borrowed==False:
            print("Please return the book")
            
    def show_info(self):
        
        if self.borrowed == True:
            print(self.title, self.author,"Borrowed") 
        else:
            print(self.title, self.author,"Available")    
 
     
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
    
    
    
book1.show_info() 

book2.show_info()       