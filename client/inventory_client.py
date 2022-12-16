import grpc

import sys
sys.path.insert(0,'C:/Users/nisch/Desktop/CMU/Sem3/API/A3/service')
import Inventory_pb2_grpc
import Inventory_pb2

#class to add an ecapsulation for the API
class InventoryClient:
    #method to return book from isbn
    def getBooks(self, isbn):
        with grpc.insecure_channel('localhost:50052', options=(('grpc.enable_http_proxy', 0),)) as channel:
            # stub instantiation
            inventory_stub = Inventory_pb2_grpc.InventoryServiceStub(channel)
            # calling GetBook
            response = inventory_stub.GetBook(Inventory_pb2.ISBN(isbnNo=isbn))
            return response

