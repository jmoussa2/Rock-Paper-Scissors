
#User choice
user_choice = input("Rock, Paper, or Scissors?")
             
#Computer choice
options_list = ['Rock', 'Paper', 'Scissors']
import random
computer_choice = random.choice(options_list)

#Reporting
print(f"I chose {user_choice}")
print(f"The Computer chose {computer_choice}")
print("------------------------------------")

tie_message = "It is a tie! Try again?"
loss_message = "Sorry, you lost."
win_message = "YOU WON! YAY!"                   

# apply logic
#Rock V. Rock
if (user_choice == "Rock") & (computer_choice == "Rock"):
    print(tie_message)

#Paper V. Rock
elif (user_choice == "Paper") & (computer_choice == "Rock"):
    print(win_message)

#Scissors V. Rock
elif (user_choice == "Scissors") & (computer_choice == "Rock"):
    print(loss_message)

#Paper V. Paper
elif (user_choice == "Paper") & (computer_choice == "Paper"):
    print(tie_message)

#Paper V. Scissors
elif (user_choice == "Paper") & (computer_choice == "Scissors"):
    print(loss_message)

#Rock V. Paper
elif (user_choice == "Rock") & (computer_choice == "Paper"):
    print(loss_message)

#Rock V. Scissors
elif (user_choice == "Rock") & (computer_choice == "Scissors"):
    print(win_message)

#Scissors V. Paper
elif(user_choice == "Scissors") & (computer_choice == "Paper"):
    print(win_message)

#Scissors V. Scissors
elif (user_choice == "Scissors") & (computer_choice == "Scissors"):
    print(tie_message)

else:
    print("There was an error in the game. Did you spell the word correctly? Capital letters and all that?")