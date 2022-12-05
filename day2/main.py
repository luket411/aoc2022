from data import practice, data as full_data

translation_map_part_one = {
    "X":"R",
    "Y":"P",
    "Z":"S",
    "A":"R",
    "B":"P",
    "C":"S"
}

POINTS_FROM = {
    "R":1, #Rock
    "P":2, #Paper
    "S":3, #Scissors
    "win":6,
    "lose":0,
    "draw":3
}

LOSES_TO = {
    'R':'P',
    'P':'S',
    'S':'R'
}

def part_1(input_data=practice):
    processed_data = [strategy.split(" ") for strategy in input_data.split("\n")]
    my_score = 0
    for [them, me] in processed_data:
        them, me = translation_map_part_one[them], translation_map_part_one[me]
        my_score += POINTS_FROM[me]
        if them == LOSES_TO[me]:
            my_score += POINTS_FROM["lose"]
        elif them == me:
            my_score += POINTS_FROM["draw"]
        else:
            my_score += POINTS_FROM["win"]

    print(my_score)


translation_map_part_two = {
    "A":"R",
    "B":"P",
    "C":"S",
    "X":"lose",
    "Y":"draw",
    "Z":"win"
}

def part_2(input_data=practice):
    processed_data = [strategy.split(" ") for strategy in input_data.split("\n")]
    my_score = 0
    for [them, strategy] in processed_data:
        them, strategy = translation_map_part_two[them], translation_map_part_two[strategy]
        my_score += POINTS_FROM[strategy]
        if strategy == "draw":                                                                                                      # if draw
            my_score += POINTS_FROM[them]                                                                                               # plus points from them
            # print(f"strategy:{strategy} means draw, and they played {them} so I have to play {them}")
        elif strategy == "win":                                                                                                     # if win
            my_score += POINTS_FROM[LOSES_TO[them]]                                                                                     # plus points from LOSES_TO[strategy]
            # print(f"strategy:{strategy} means win, and they played {them} so I have to play {LOSES_TO[them]}")
        else:                                                                                                                       # else lose
            my_score += POINTS_FROM[LOSES_TO[LOSES_TO[them]]]                                                                           # plus points from LOSES_TO[LOSES_TO[strategy]]
            pass                                        
            # print(f"strategy:{strategy} means lose, and they played {them} so I have to play {LOSES_TO[LOSES_TO[them]]}")

    return(my_score)


if __name__ == "__main__":
    part_1(full_data)
    part_2(full_data)