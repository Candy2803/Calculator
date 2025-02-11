import random

def game():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    print("Welcome to Rock, Paper, Scissors game")
    print("Choices are: Rock, Paper, Scissors.")
    
    users_choice = input("Choice? ")
    
    if users_choice not in choices:
        print("Invalid choice")
        return
    
    print(f"You chose {users_choice} while the computer chose {computer_choice}.")
    
    if users_choice == computer_choice:
        print("Its a Tie")
    elif (users_choice == 'Rock' and computer_choice == 'Scissors') or \
         (users_choice == 'Paper' and computer_choice == 'Rock') or \
         (users_choice == 'Scissors' and computer_choice == 'Paper'):
            print("You Win!")
    else:
        print("You Lose!")
        
        
game()