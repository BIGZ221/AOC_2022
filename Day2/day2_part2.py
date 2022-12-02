
with open("input.txt") as f:
    data = f.read()

rounds = data.split("\n")

def loss(opponent):
    if opponent == "A": # Rock
        return 3
    if opponent == "B": # Paper
        return 1
    if opponent == "C": # Scissors
        return 2

def draw(opponent):
    if opponent == "A": # Rock
        return 1
    if opponent == "B": # Paper
        return 2
    if opponent == "C": # Scissors
        return 3

def win(opponent):
    if opponent == "A": # Rock
        return 2
    if opponent == "B": # Paper
        return 3
    if opponent == "C": # Scissors
        return 1

def score_hand(opponent, outcome):
    hand = 0
    if outcome == "X": # Loss
        hand += 0
        hand += loss(opponent)
    if outcome == "Y": # Draw
        hand += 3
        hand += draw(opponent)
    if outcome == "Z": # Win
        hand += 6
        hand += win(opponent)
    return hand

total = 0
for round in rounds:
    opponent, outcome = round.split()
    total += score_hand(opponent, outcome)

print(total)
