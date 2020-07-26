# get user input for a single word describing something that can be read saved in a variable called can_read
# get user input for 3 things can be read. save in a variable called can_read_things
# print true if the can_read string is found in the can_read_things string variable


# 1 -- get 1 word input for can_read variable

can_read=input("enter 1 word that can be read: ")

# 2 -- get 3 things input for can_read_things variable

can_read_things=input("enter 3 items that can be read: ")

# 3 -- print True if can_read is in can_read_things

print(can_read in can_read_things)

# challenge: format the output to read "item found = True" (or false)

print("item found =", can_read in can_read_things)
