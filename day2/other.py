from data import practice, data as full_data

strategy_one_score_map = {
    # They chose Rock
    "A X":3+1,  # I chose Rock
    "A Y":6+2,  # I chose Paper
    "A Z":+0+3, # I chose Scissors
    # They chose Paper
    "B X":0+1,  # I chose Rock
    "B Y":3+2,  # I chose Paper
    "B Z":6+3,  # I chose Scissors
    # They chose Scissors
    "C X":6+1,  # I chose Rock
    "C Y":0+2,  # I chose Paper
    "C Z":3+3   # I chose Scissors
}

strategy_two_score_map = {
    # They chose Rock
    "A X":0+3,  # I need to lose and so chose scissors
    "A Y":3+1,  # I need to draw and so chose rock
    "A Z":6+2,  # I need to win and so chose paper
    # They chose Paper
    "B X":0+1,  # I need to lose and so chose rock
    "B Y":3+2,  # I need to draw and so chose paper
    "B Z":6+3,  # I need to win and so chose scissors
    # They chose Scissors
    "C X":0+2,  # I need to lose and so chose paper
    "C Y":3+3,  # I need to draw and so chose scissors
    "C Z":6+1   # I need to win and so chose rock
}

def one_liner(dataset, strategy):
    return sum([strategy[instruction] for instruction in dataset.split("\n")])

print(one_liner(full_data, strategy_one_score_map))
print(one_liner(full_data, strategy_two_score_map))
