import get_book_titles
import inventory_client
from unittest.mock import Mock, MagicMock

# if isbn and book exist
def test1():
    client = inventory_client.InventoryClient()
    mockBook = {"isbn":"1234", "title":"testTitle",
                "author":"testAuthor", "genre":"THRILLER","publishingYear":1996}
    client.getBooks = MagicMock(return_value=mockBook)
    response = client.getBooks("1234")
    assert response == mockBook
    print("test1 passed")

# if isbn does not exist
def test2():
    client = inventory_client.InventoryClient()
    mockBook = {}
    client.getBooks = MagicMock(return_value=mockBook)
    response = client.getBooks("1236")
    assert response == mockBook
    print("test2 passed")


# test with server on
def test3():
    response = get_book_titles.main()
    book1 = response[0]
    book2 = response[1]
    assert book1.isbn == "1234"
    assert book1.author == "testAuthor1"
    assert book1.title == "testTitle1"
    assert book1.publishingYear == 2000

    assert book2.isbn == "1235"
    assert book2.author == "testAuthor2"
    assert book2.title == "testTitle2"
    assert book2.publishingYear == 2001
    print("test3 passed")

if __name__ == '__main__':
    test1()
    test2()
    test3()