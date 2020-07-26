# get input for test
input_test=input("enter some things eaten in the last 24 hours: ")

# print True if "dairy" is in the input or False if not
print("dairy" in input_test)
print("It is", "dairy" in input_test, 'that "' + input_test + '"', 'contains "dairy"' )

# Check if "nuts" are in the input
print("nuts" in input_test)

# Check if "seafood" is in the input
print("Seafood" in input_test)

# Check if "chocolate" is in the input
print("chocolate" in input_test)

# Challenge: make your code work for input regardless of case
print("nuts".casefold() in input_test.casefold())
