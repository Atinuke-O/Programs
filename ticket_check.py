# Program: ticket_check() - finds out if a seat is available
        # Call ticket_check() function with 2 arguments: section and seats requested and return True or False
              # section is a string and expects: general, floor
              # seats is an integer and expects: 1 - 10
                  # Check for valid section and seats
                      # if section is general (or use startswith "g")
                      # if seats is 1-10 return True
                      # if section is floor (or use starts with "f")
                      # if seats is 1-4 return True
                            # otherwise return False
                            
                         
def ticket_check ():
    section=input("Enter section ")
    if section.startswith("g"): 
        seats=input("Enter number of seats ")
        if int(seats) in range(1, 10):
            available = "True"
            return available
        else:
            unavailable = "False"
            return unavailable
    if section.startswith("f"):
        seats=input("Enter number of seats ")
        if int(seats) in range (1, 4):
            available = "True"
            return available
        else:
            unavailable = "False"
            return unavailable
    else:
        print ("invalid entry")
        
ticket_check()
