
with open("input.txt") as f:
    data = f.read()

rounds = data.split("\n")

def score_hand(opponent, player):
    hand = 0
    if player == "X": # Rock
        hand += 1
        if opponent == "A": # Rock
            hand += 3 # Draw
        if opponent == "B": # Paper
            hand += 0 # Loss
        if opponent == "C": # Scissors
            hand += 6 # Win
    if player == "Y": # Paper
        hand += 2
        if opponent == "A": # Rock
            hand += 6 # Win
        if opponent == "B": # Paper
            hand += 3 # Draw
        if opponent == "C": # Scissors
            hand += 0 # Loss
    if player == "Z": # Scissors
        hand += 3
        if opponent == "A": # Rock
            hand += 0 # Loss
        if opponent == "B": # Paper
            hand += 6 # Win
        if opponent == "C": # Scissors
            hand += 3 # Draw
    return hand

total = 0
for round in rounds:
    opponent, player = round.split()
    total += score_hand(opponent, player)

print(total)
