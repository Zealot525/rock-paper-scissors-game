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

print("Welcome to the Rock Scissors Paper Game!")
RSP = [rock, scissors, paper]
user_input = int(input("To get started, type '0' for Rock, '1' for Scissors, '2' for Paper!\n"))
if user_input>=3 or user_input <0:
  print("you typed something else, you LOSE by not following instructions :)")
else:
  print(f"You chose: \n{RSP[user_input]}")

  import random
  computer_input = random.randint(0,2)
  print(f"Computer chose: \n{RSP[computer_input]}")


  if user_input == computer_input:
    print("It's a tie! Better luck next time!\nGame Over.")
  elif user_input == 2 and computer_input == 0:
    print("Yeah! You win!\nWanna try your luck again?")
  elif user_input == 0 and computer_input == 2:
    print("Ouch! Better luck next time!\nGame Over.")
  elif user_input > computer_input:
    print("Ouch! Better luck next time!\nGame Over.")
  elif user_input < computer_input:
    print("Yeah! You win!\nWanna try your luck again?")
