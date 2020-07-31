#----------Rainbow colors---------#
# ask for input of a favorite rainbow color first letter: ROYGBIV
# Using if, elif, and else:

  #print the color matching the letter
  #     R = Red
  #     O = Orange
  #     Y = Yellow
  #     G = Green
  #     B = Blue
  #     I = Indigo
  #     V = Violet
  #     else print "no match"
  

rainbow_colors = input("Enter the first letter of your favorite rainbow color: ")

if rainbow_colors.upper() == "R":
    print ("Red")
elif rainbow_colors.upper() == "O":
    print ("Orange")
elif rainbow_colors.upper() == "Y":
    print ("Yellow")
elif rainbow_colors.upper() == "G":
    print ("Green")
elif rainbow_colors.upper() == "B":
    print ("Blue")
elif rainbow_colors.upper() == "I":
    print ("Indigo")
elif rainbow_colors.upper() == "V":
    print ("Violet")
else:
    print ("no match")
    
# make the code above into a function rainbow_color() that has a string parameter, 
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.

def rainbow_colors ():
    colors = input("Enter the first letter of your favorite rainbow color: ")
    if colors.upper() == "R":
        return "Red"
    elif colors.upper() == "O":
        return "Orange"
    elif colors.upper() == "Y":
        return "Yellow"
    elif colors.upper() == "G":
        return "Green"
    elif colors.upper() == "B":
        return "Blue"
    elif colors.upper() == "I":
        return "Indigo"
    elif colors.upper() == "V":
        return "Violet"
    else:
        return ("no match")
    
myfavorite_color = rainbow_colors()
print (myfavorite_color)

    #-------------------------#

# Create function age_20() that adds or subtracts 20 from your age for a return value based on current age (use if)

  #call the funtion with user input and then use the return value in a sentence
  #example age_20(25) returns 5:
  #"5 years old, 20 years difference from now"

def age_20(age):
    if int(age) >= 20:
        full_function = (int(age) - 20)
        return full_function
    if int(age) < 20:
        fill_function = (int(age) + 20)
        return fill_function
    else:
        return "invalid entry"
    
agez = (age_20(input("Enter your age: ")))    
print(agez, "years old, 20 years difference from now")

    #-------------------------#

#create a function rainbow_or_age that takes a string argument

  #if argument is a digit return the value of calling age_20() with the str value cast as int
  #if argument is an alphabetical character return the value of calling rainbow_color() with the str
  #if neither return FALSE

def rainbow_or_age(ar = "constant"):
    if ar.isdigit() == True:
        return age_20(ar)
    elif ar.isalpha() == True:
        return rainbow_colors()
    else:
        return "FALSE"
    
print(rainbow_or_age ("6"))
print(rainbow_or_age())
