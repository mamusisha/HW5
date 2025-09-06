from datetime import datetime
import random

secret_number = random.randint(1, 20)
start_time = datetime.now()
time_limit = 5

while (datetime.now() - start_time).total_seconds() < time_limit:
    guess = input("enter your guess: ")
    if int(guess) == secret_number:
        print("you guessed right!")
        break
    else:
        print("you guessed wrong, try again")

else:
    print("timeout! The number was:", secret_number)