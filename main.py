import random 
number = random.randint(1, 100)
attempts = 0

while True:
    print("Guess a number between 1 and 100")
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        print("Do you want to play again? (yes/no)")
        play_again = input().strip().lower()
        if play_again == "yes":
            number = random.randint(1, 100)
            attempts = 0
        else:
            print("Thanks for playing!")
            break



    
  