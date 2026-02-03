import app as dr
from app import Player
import os

while True:
    try:
        num_of_players = int(input("Enter # of people playing -> "))
        break
    except ValueError:
        print("Invalid input.\nTry again.")

for i in range(num_of_players):
    name = input("Enter your name:").title().strip()
    player = Player(name)
   # player.players.append(name)

score_goal = int(input("Enter the score goal for this game -> "))
roller = dr.Dice_Roller()
# round loop:
# determine player
# while player does not choose to stop or farkle
# player rolls
# ROUND points are determined and summed
# player continues to roll to build on round points or stop
# if player has points and chooses to stop, those points are added to their score

# while found_winner = false
# for each player - loop until the player's turn ends (stop or farkle)
# after each players turn, check for winner and set flag if won
found_winner = False
round_score = 0
round = 1
while not found_winner:
    for player in Player.players:
        #print(player.name)
        # have a function to handle the players turn
        # player.score += play_round(player, dice)
        # if player.score >= target_score:
        # found_winner = True #set flag to exit loop

# find who had the highest score, and declare as winner
        print()
        print(f"Round {round}.\n{player.name}'s turn.")
        print(
            f"{player.name} do you wish to (roll or bank) your points?: ")
        while True:
            print("Please enter \"r\" to roll or \"b\" to bank: ")
            choice = input("Choice -> ").lower().strip()
            if choice == "r":
                roller.roll()
                roller.print_dice()
                round_score += roller.determine_points()
                print(
                    f"{player.name} has {round_score} points so far this round.")
                print()

                if roller.determine_points() == 0:
                    print(f"{player.name} have farkled.")
                    print(
                        f"{player.name} gets 0 points for this round.")
                    print()
                    player.score -= round_score
                    break

            if choice == "b":
                player.score += round_score
                print(f"{player.name} has {player.score} points.")
                round_score = 0
                break
    
        if player.score >= score_goal:
            print(f"{player.name} reached the score goal.")
            winner = Player.players[0]
            for player in Player.players:
                if player.score > winner.score:
                    winner = player
                    print(f"Winner is {winner.name} with {winner.score} points!")
            found_winner = True

        if num_of_players == 1 and player.score >= score_goal:
            print(f"{player.name} has won!")
            found_winner = True

    round += 1

# try:
#     player_index += 1
#     print(f"Last chance {player.players[player_index]}")
#     print(f"You have {player.score} right now.")
#     print(
#         f"{player.players[player_index]} do you wish to (roll or bank) your points?: ")
#     print("Please enter \"roll\" or \"bank\" ")
#     choice = input("Choice -> ")
#     if choice == "roll":
#         roller.roll()
#         roller.print_dice()
#         player.score += roller.determine_points()
#         print(f"{player.players[player_index]} has {player.score} points.")

#         if roller.determine_points() == 0:
#             print(f"{player.players[player_index]} have farkled.")
#             print(
#                 f"{player.players[player_index]} get 0 points for this round.")
#             player.score = 0
#             player_index += 1

#     elif choice == "bank":
#         print(f"{player.players[player_index]} has {player.score} points.")
#         player_index += 1

# except IndexError:
#     player_index = 0

# roller.roll()
# roller.print_dice()

# print()
# print(f"Round {round}.\n{player.players[player_index]}'s turn.")
# if roller.determine_points() == 0:
#     print(f"{player.players[player_index]} have farkled.")
# player.score += roller.determine_points()
# print(player.score)
