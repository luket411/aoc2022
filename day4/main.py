from data import practice, full_data
import numpy as np

def is_contained(range_1, range_2):
    return (int(range_1[0]) <= int(range_2[0])) and (int(range_1[1]) >= int(range_2[1]))
    

def part_1(input_data=practice):
    num_pairs = 0
    for pair in input_data.split("\n"):
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        if is_contained(range_1, range_2) or is_contained(range_2, range_1):
            num_pairs += 1
    
    return num_pairs


def part_2(input_data=practice):
    overlap = 0
    no_overlap = 0
    for pair in input_data.split("\n"):
        range_1, range_2 = pair.split(",")
        range_1, range_2 = range_1.split("-"), range_2.split("-")
        range1_start, range1_stop = int(range_1[0]), int(range_1[1])
        range2_start, range2_stop = int(range_2[0]), int(range_2[1])
        if range1_stop >= range2_start and range2_stop >= range1_start:
            overlap += 1
            
    return overlap

# Function but 10x slower
def part_2_2(input_data = practice):
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


if __name__ == "__main__":
    print(part_1())
    print(part_1(full_data))
    print(part_2())
    print(part_2(full_data))

    # import timeit
    # print(timeit.timeit(lambda:part_2(full_data), number=10000))      # Approx 5 seconds
    # print(timeit.timeit(lambda:part_2_2(full_data), number=10000))    # Approx 50 seconds