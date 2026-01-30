import app as dr
from app import Player

round = 1
num_of_players = int(input("Enter # of people playing -> "))
for i in range(num_of_players):
    name = input("Enter your name:").title().strip()
    player = Player(name)
    player.players.append(name)

roller = dr.Dice_Roller()
roller.roll()
roller.print_dice()
print()
print(f"Round {round}.\n{player.players[0]}'s turn.")
roller.determine_points()

print(player.score)

# for i in range(len(player_names)):
#     if player_names[i] >= score_goal:
#         print(f"{player_names[i].title()} has reached the score goal!")
#         break