import random

def guessing():
    generated_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = input("Enter number: ")

        if not guess.isdigit():
            print(f"{guess} is not a number")
            continue
        
        guess = int(guess)
        attempts += 1
        
        
        if guess > generated_number:
            print(f"Your guess is greater than the generated number ")
        elif guess < generated_number:
            print(f"Your guess is lower than the generated number ")
        else:
            print(f"Correct! You got the number after {attempts} attempts")
            break
    else:
         print(f"Game over! You used all your {max_attempts} attempts") 
    
guessing()