import random

roll = random.randint(1, 6)
guess = int(input("Guess the number: "))
if guess == roll:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")

print(f"The computer rolled a {roll}!")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter rock, paper, or scissors: ")
print(f"The computer chose: {computer_choice}")