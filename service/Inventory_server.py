import grpc
import Inventory_pb2
import Inventory_pb2_grpc
from concurrent import futures


# Inventory Service Server implement InventoryServiceServicer
class InventoryServiceServer(Inventory_pb2_grpc.InventoryServiceServicer):
    database = {}

    def __init__(self):
        book1 = Inventory_pb2.Book()
        book1.isbn = "1234"
        book1.author = "testAuthor1"
        book1.title = "testTitle1"
        book1.genre = Inventory_pb2.Book.THRILLER
        book1.publishingYear = 2000
        self.database[book1.isbn] = book1

        book2 = Inventory_pb2.Book()
        book2.isbn = "1235"
        book2.author = "testAuthor2"
        book2.title = "testTitle2"
        book2.genre = Inventory_pb2.Book.FICTION
        book2.publishingYear = 2001
        self.database[book2.isbn] = book2

    # implementing create book
    def CreateBook(self, request, context):
        # fetching all parameters
        isbn = request.isbn
        title = request.title
        author = request.author
        genre = request.genre
        publishing_year = request.publishingYear
        # creating book object
        book = Inventory_pb2.Book()
        book.isbn = isbn
        book.genre = genre
        book.publishingYear = publishing_year
        book.title = title
        book.author = author
        # check for if isbn already exist
        if isbn in self.database:
            return Inventory_pb2.Result(isbn="", message="isbn already exist!")
        # check if title or author is empty
        elif title == '' or author == '':
            return Inventory_pb2.Result(isbn="", message="title and author should not be empty")
        # adding the book to database
        self.database[isbn] = book
        return Inventory_pb2.Result(isbn=isbn, message="successfully created book")

    # get book given isbn
    def GetBook(self, request, context):
        # if isbn exist, return it else return nothing
        if request.isbnNo in self.database:
            return self.database[request.isbnNo]
        else:
            return Inventory_pb2.Book()


# main server code
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    Inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


main()
