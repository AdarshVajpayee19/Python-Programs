Number_to_be_guessed =  50
# No. of Guesses 6
# Print No of Guesses left
# Number of Guesses He took To finish
# Gameover

No_of_Guesses = 6
init_guesses = 0
while init_guesses < No_of_Guesses :
    User_guesses = int(input("Enter the number between (1 to 100) : "))
    if Number_to_be_guessed > User_guesses:
        print("Enter Some Greater Value To Get Answer.")
        init_guesses = init_guesses + 1
    elif Number_to_be_guessed < User_guesses:
        print("Enter Some lesser Value To Get Answer.")
        init_guesses = init_guesses + 1
    else:
        print("Congrats You Won")
        print("You took ",init_guesses+1," number of guesses.")
        print(No_of_Guesses - init_guesses-1," no. of Guesses left.")
        exit()
print("Limited Number of Guesses Over.")
print("*********GAME OVER*********")
print("You Lose")

