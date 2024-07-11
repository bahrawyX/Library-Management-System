from models.book import Book
from repository.file_manager import DataBaseHandler


class BookRepository:
    
    
    
    def __init__(self):
        self.file_manager  =DataBaseHandler()
        self.books = self.file_manager.load()
        self.cnt = self.books[len(self.books)-1].isbn+1
        
        
    
    def add_book(self, book):
        book.isbn = self.cnt
        self.cnt += 1 
        self.books.append(book)
        self.file_manager.save(books=self.books)
        return book.isbn

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.isbn == book_id:
                return book
        return None

    def update_book(self, book):
        for i in range(len(self.books)):
            if self.books[i].isbn == book.isbn:
                self.books[i] = book
                self.file_manager.save(books=self.books)
                return True
        
        return False

    def delete_book(self, book_id):
        for i in range(len(self.books)):
            if self.books[i].isbn == book_id:
                del self.books[i]
                self.file_manager.save(books=self.books)
                return True
        return False
    
    

    