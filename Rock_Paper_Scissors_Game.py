rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user >= 3 or user < 0:
  print("Invalid option")
else:
  choices = [rock, paper, scissors]
  npc = random.randint(0,2)
  
  print(choices[user])
  print("Computer chose: \n" + choices[npc])
  
  
  if user == npc:
    print("It's a draw!")
  elif user == 0 and npc == 1:
    print("You lose")
  elif user == 0 and npc == 2:
    print("You win!")
  elif user == 1 and npc == 0:
    print("You win!")
  elif user == 1 and npc == 2:
    print("You lose")
  elif user == 2 and npc == 0:
    print("You lose")
  elif user == 2 and npc == 1:
    print("You win!")
  
