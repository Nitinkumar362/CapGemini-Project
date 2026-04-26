#  this tha Stone paper scissors game by using python programs

# 0 for Rock
# 1 for Paper
# 2 for Scissor

# User's choice (0,1,2)             # Computer's choice (0,1,2)
# 1       0                                 0    Draw
# 2       0                                 1    win
# 3       0   win                           2
# 4       1   win                           0
# 5       1                                 1    Draw
# 6       1                                 2    win
# 7       2                                 0    win
# 8       2   win                           1
# 9       2                                 2    Draw

# Thair are three case of


import random

user_choice = int(input("Enter your choice : Type 0 for Rock , 1 for Paper , 2 for scissor : "))
if user_choice >= 3 or user_choice < 0:
    print("You entered a invalid Number , You lose.")
else:
    computer_choice = random.randint(0, 2)
    print("Computer chose :")
    print(computer_choice)

    if computer_choice == user_choice:
        print("It's a draw.")

    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")

    elif user_choice == 0 and computer_choice == 2:
        print("You win.")

    # elif user_choice == 2 and computer_choice == 0:
    #     print("You win.")

    elif computer_choice > user_choice:
        print("You lose.")

    elif computer_choice > user_choice:
        print("You win.")

    # elif computer_choice > user_choice:
    #     print("You win.")
