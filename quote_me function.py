# Program: quote_me() Function
    # quote_me takes a string argument and returns a string that will display surrounded with added double quotes if printed
        #check if passed string starts with a double quote ("\""), then surround string with single quotations
        #if the passed string starts with single quote, or if doesn't start with a quotation mark, then surround with double quotations
        #Test the function code passing string input as the argument to quote_me()
       
def quote_me():
    string=input("Enter a string: ")
    quote_maker = ("'" + string + "'")
    quote_maker2 = ("\"" + string + "\"")
    if string.startswith("\""):
        print (quote_maker)
    elif string.startswith("'"):
        print (quote_maker2)
    else:
        print (quote_maker2)

quote_me()
