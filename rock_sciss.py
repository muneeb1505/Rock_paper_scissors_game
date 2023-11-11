import random

options = ["rock", "paper", "scissors"]

while(True):
 user_choice = input("\nChoose rock, paper or scissors : ")
 computer_choice = random.choice(options)

 print("You choose",user_choice)
 print("Computer choose",computer_choice)

 if user_choice == computer_choice:
    print("Game draw!")

 elif user_choice == "rock" and computer_choice == "scissors":
  print("You win!")

 elif user_choice == "paper" and computer_choice == "rock":
  print("You win!")

 elif user_choice == "scissors" and computer_choice =="paper":
  print("You win!")
  
 else:
    print("Computer win!")