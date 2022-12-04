from data import practise, full_data
import numpy as np

def is_contained(range_1, range_2):
    return (int(range_1[0]) <= int(range_2[0])) and (int(range_1[1]) >= int(range_2[1]))
    

def part_1(input_data=practise):
    num_pairs = 0
    for pair in input_data.split("\n"):
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        if is_contained(range_1, range_2) or is_contained(range_2, range_1):
            num_pairs += 1
    
    return num_pairs

# This one doesnt work
def part_2(input_data=practise):
    overlap = 0
    no_overlap = 0
    for pair in input_data.split("\n"):
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        if int(range_1[1]) >= int(range_2[0]):
            overlap += 1
            
    return overlap
        
# This one works
def part_2_2(input_data = practise):
    overlap = 0
    for pair in input_data.split("\n"):
        contents = np.zeros(101)
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        range1_start, range1_stop = int(range_1[0]), int(range_1[1])
        range2_start, range2_stop = int(range_2[0]), int(range_2[1])
        
        contents[range1_start-1:range1_stop] += 1
        contents[range2_start-1:range2_stop] += 1
        
        if 2 in contents:
            overlap += 1
    
    return overlap

"""
# Code here is to find the case where one function worked and the other didn't
#

def has_overlap_method_one(range_1, range_2):
    return int(range_1[1]) >= int(range_2[0])

def has_overlap_method_two(range_1, range_2):
    contents = np.zeros(101)
    range1_start, range1_stop = int(range_1[0]), int(range_1[1])
    range2_start, range2_stop = int(range_2[0]), int(range_2[1])
    
    contents[range1_start-1:range1_stop] += 1
    contents[range2_start-1:range2_stop] += 1
    
    return 2 in contents

def part_2_main(input_data = practise):
    for pair in input_data.split("\n"):
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        if has_overlap_method_one(range_1, range_2) and not has_overlap_method_two(range_1, range_2):
            print(range_1, range_2)
        break
"""


if __name__ == "__main__":
    # print(part_1())
    # print(part_1(full_data))
    # print(part_2_2())
    # print(part_2_2(full_data))
    part_2_main(full_data)