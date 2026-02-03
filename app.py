import random

#just showing a pull
class Dice_Roller:
    # shared variable
    dice_art: dict[int, tuple] = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }

    def __init__(self, num_of_dice: int = 3):
        self.values = []
        for num in range(num_of_dice):
            self.values.append(0)

    def roll(self) -> None:
        for die in range(len(self.values)):
            self.values[die] = random.randint(1, 6)

    def print_dice(self) -> None:
        for line in range(5):
            for die in self.values:
                print(Dice_Roller.dice_art.get(die, ())[line], end="")
            print()

    def determine_points(self):
        # deterimine if they are all the same:
        diceSet = set(self.values)
        if len(diceSet) == 1:
            return 500
        score = 0
        for die in self.values:
            if die == 1:
                score += 100
            if die == 5:
                score += 50
            else:
                score += 0

        return score

    def get_total(self) -> int:
        total = 0
        for die in self.values:
            total += die

        return total


class Player:
    players = []

    def __init__(self, name: str, score: int = 0) -> None:
        self.name = name
        self.score = score
        Player.players.append(self)