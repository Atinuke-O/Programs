# create letter_guess() function that gives user 3 guesses
    # takes a letter character argument for the answer letter
    # gets user input for letter guess
    # calls check_guess() with answer and guess
    # End letter_guess if
    # check_guess() equals True, return True or after 3 failed attempts, return False


def letter_guess():
    
    call = check_guess (input("Guess the letter: "), "S") 
    
    if call == "True":
        return "True"
    
    if call == "False":
        call2 = check_guess (input("Try again: "), "S")
        if call2 == "True":
            return "True"
        
    if call2 == "False":
        call3 = check_guess (input("Try last: "), "S")
        if call3 == "True":
            return "True"
        
    if call3 == "False":
            return "You ran out of attempts"
    else:
        return "False"

    
letter_guess()
