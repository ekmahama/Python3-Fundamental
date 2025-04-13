import random
comp_choice = random.choice(["paper", "scissors", "rock"])
user_choice = input("Do you want rock, paper or scissors?: ")

if comp_choice == user_choice:
    print("it is a Tie")
elif user_choice == "scissors" and comp_choice == "paper":
    print("You win")
elif user_choice == "rock" and comp_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and comp_choice == "rock":
    print("You win!")
else:
    print("Computer wins!")
