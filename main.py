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

#Write your code below this line 👇
user_input = int(input("type '0' for rock type '1' paper type '2' for scissors"))
list = [rock, paper, scissors]
if user_input >= 3 or user_input < 0 :
  print('you typed an invalid number') 
else :
  print(f'user chose: {user_input} \n {list[user_input]}')

computer_choice= random.randint(0,2)
print(f'computer chose: {computer_choice} \n {list[computer_choice]}')

if user_input >= 3 or user_input < 0 :
  print('you typed an invalid number') 
elif user_input == 0 and computer_choice == 2:
  print('you win')
elif computer_choice > user_input:
  print('you lose')
elif computer_choice < user_input:
  print('you win')
elif computer_choice == user_input:
  print('its a draw')
