# Program: str_analysis() Function
      # Create the str_analysis() function that takes a string argument. In the body of the function:
      
            # Check if string is digits
                  # if digits: convert to int and check if greater than 99
                  # if greater than 99, print a message about a "big number"
                  # if not greater than 99, print message about "small number"
                  # if not digits: check if string isalpha
                  # if isalpha print message about being all alpha
                  # if not isalpha print a message about being neither all alpha nor all digit
                  # call the function with a string from user input
                  
def str_analysis(string):
    if string.isdigit():
        intt = int(string)
        if intt > 99:
            print ("This is a big number")
        if intt <= 99:
            print ("This is a small number")
    elif string.isalpha():
        print ("This is an alphabetic character")
    else:
        print ("This is neither alphabetical nor all digit")

my_num = input()
str_analysis(my_num)
