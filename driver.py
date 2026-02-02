import app as dr
from app import Player

round = 1
player_index = 0
num_of_players = int(input("Enter # of people playing -> "))
for i in range(num_of_players):
    name = input("Enter your name:").title().strip()
    player = Player(name)
    player.players.append(name)

score_goal = int(input("Enter the score goal for this game -> "))
roller = dr.Dice_Roller()
#round loop:
#determine player
#while player does not choose to stop or farkle
#player rolls
#ROUND points are determined and summed
#player continues to roll to build on round points or stop
#if player has points and chooses to stop, those points are added to their score

#while found_winner = false
#for each player - loop until the player's turn ends (stop or farkle)
# after each players turn, check for winner and set flag if won
found_winner = True
while found_winner:
    try:
        print()
        print(f"Round {round}.\n{player.players[player_index]}'s turn.")
        print(f"{player.players[player_index]} do you wish to (roll or bank) your points?: ")
        print("Please enter \"roll\" or \"bank\" ")
        choice = input("Choice -> ")
        if choice == "roll":
            roller.roll()
            roller.print_dice()
            player.score += roller.determine_points()
            print(f"{player.players[player_index]} has {player.score} so far this round.")
    
            if roller.determine_points() == 0:
                print(f"{player.players[player_index]} have farkled.")
                print(f"{player.players[player_index]} get 0 points for this round.")
                player.score = 0
                player_index += 1

        elif choice == "bank":
            print(f"{player.players[player_index]} has {player.score} points.")
            player_index += 1

        if player.score >= score_goal:
            print(f"{player.players[player_index]} has won the game!")
            found_winner = False

    except IndexError:
        player_index = 0
        if player_index == 0:
            round += 1

try:
    player_index += 1
    print(f"Last chance {player.players[player_index]}")
    print(f"You have {player.score} right now.")
    print(f"{player.players[player_index]} do you wish to (roll or bank) your points?: ")
    print("Please enter \"roll\" or \"bank\" ")
    choice = input("Choice -> ")
    if choice == "roll":
        roller.roll()
        roller.print_dice()
        player.score += roller.determine_points()
        print(f"{player.players[player_index]} has {player.score} points.")

        if roller.determine_points() == 0:
            print(f"{player.players[player_index]} have farkled.")
            print(f"{player.players[player_index]} get 0 points for this round.")
            player.score = 0
            player_index += 1

    elif choice == "bank":
        print(f"{player.players[player_index]} has {player.score} points.")
        player_index += 1
        
except IndexError:
    player_index = 0

# roller.roll()
# roller.print_dice()

# print()
# print(f"Round {round}.\n{player.players[player_index]}'s turn.")
# if roller.determine_points() == 0:
#     print(f"{player.players[player_index]} have farkled.")
# player.score += roller.determine_points()
# print(player.score)