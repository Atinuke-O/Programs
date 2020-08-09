# Program: shirt order
    # First get input for color and size
         # White has sizes L, M
         # Blue has sizes M, S
              # print available or unavailable, then
              # print the order confirmation of color and size

#-hint: set a variable "available = False" before nested if statements and
#-change to True if color and size are avaliable


available = True

if available:
    color = input ("Enter color white or blue: ")
    if color.title() == "White":
        size = input ("Enter size L or M: ")
        if size.upper() == "M":
            print ("available")
            print("Your order is: one " + color + " shirt size " + size.upper())
        elif size.upper() == "L":
            print ("available")
            print("Your order is: one " + color + " shirt size " + size.upper())
        else:
            print ("Invalid entry. you can only enter size L or M")
    elif color.title() == "Blue":
        size = input ("Enter size M, L, or S: ")
        if size.upper() == "M":
            print ("available")
            print("Your order is: one " + color + " shirt size " + size.upper())
        elif size.upper() == "S":
            print ("available")
            print("Your order is: one " + color + " shirt size " + size.upper())
        else:
            print ("Invalid entry. you can only enter size L or M")
    else:
        print ("unavailable")
else:
    color = input ("Enter color white or blue: ")
    if color.title() == "White":
        size = input ("Enter size M, L, or S: ")
        if size.upper() == "M":
            print ("unavailable")
        elif size.upper() == "L":
            print ("unavailable")
        else:
            print ("Invalid entry. you can only enter size L or M")
    elif color.title() == "Blue":
        size = input ("Enter size M, L, or S: ")
        if size.upper() == "M":
            print ("unavailable")
        elif size.upper() == "S":
            print ("unavailable")
        else:
            print ("Invalid entry. you can only enter size L or M")
    else:
        print ("unavailable")
