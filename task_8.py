from datetime import datetime, timedelta
import random

start = datetime.now()

player1_finish = start + timedelta(seconds=random.randint(5, 20))
player2_finish = start + timedelta(seconds=random.randint(5, 20))

player1_time = (player1_finish - start).seconds
player2_time = (player2_finish - start).seconds

print(f"player 1 finished in {player1_time} seconds")
print(f"player 2 finished in {player2_time} seconds")

if player1_time < player2_time:
    print("player 1 wins!")
elif player2_time < player1_time:
    print("player 2 wins!")
else:
    print("it's a tie!")