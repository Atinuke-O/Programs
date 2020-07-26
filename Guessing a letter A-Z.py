      # check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)

# - if guess is not an alpha character print invalid and return False
# - test and print if guess is "high" or "low" and return False
# - test and print if guess is "correct" and return True
# - call check_guess with user input


def check_guess(guess, letter="R"):
    
    if guess.isalpha() == False:
        return "False"
    elif guess.upper() > letter:
        return "False"
    elif guess.upper() < letter:
        return "False"
    else:
        return "True"

check_guess ("r")
check_guess(input(), "F")
    
