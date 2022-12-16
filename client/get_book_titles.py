import inventory_client as client

#to create a list of response from 2 hardcoded isbn and printing it
def main():
    #hardcoding 2 isbn
    isbns = ["1234","1235"]
    inventory_client = client.InventoryClient()
    #creating a dictionary of response
    finalResponse = []
    for no in isbns:
        response = inventory_client.getBooks(no)
        finalResponse.append(response)
    return finalResponse

if __name__ == '__main__':
    response = main()
    print(response)