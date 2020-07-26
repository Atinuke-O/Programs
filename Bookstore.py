# bookstore() takes 2 string arguments: book & price
# bookstore returns a string in sentence form
# bookstore() should call title_it_rtn() with book parameter
# gather input for book_entry and price_entry to use in calling bookstore()
# print the return value of bookstore()
    #--example of output: Title: The Adventures Of Sherlock Holmes, costs $12.99
    
# create, call and test bookstore() function

def bookstore (book, price):
    string = ("Title: " + book + ", costs " + price)
    return string

book_entry=input("Enter the name of a book: ")
price_entry=input("Enter price: ")

bookcall1 = bookstore(title_it_rtn(book_entry), price_entry)

print(bookcall1)
