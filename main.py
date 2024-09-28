import random

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

# Write your code below this line 👇

game_images = [rock, paper, scissors]
computers_choice = random.randint(0, 2)
users_choice = int(input("What do you choose? Press 0 for rock, 1 for paper, 2 for scissors: "))
print(game_images[users_choice])

print("Computer choose: ")
print(game_images[computers_choice])

if users_choice >= 3 or users_choice < 0:
    print("You typed an invalid number, You Lose!")
elif users_choice == 0 and computers_choice == 1:
    print("Computer wins")
elif users_choice == 0 and computers_choice == 2:
    print("You Win")
elif users_choice == 1 and computers_choice == 0:
    print("You Win")
elif users_choice == 1 and computers_choice == 2:
    print("Computer wins")
elif users_choice == 2 and computers_choice == 0:
    print("Computer wins")
elif users_choice == 2 and computers_choice == 1:
    print("You Win")
else:
    print("It's a draw")
