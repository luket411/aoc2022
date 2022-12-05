from data import day1_practice, day1_data

def part_1(data=day1_practice):
    calorie_counter = 0
    largest_calorie_count = 0
    for num_string in data.split("\n"):
        if num_string == "":
            if calorie_counter > largest_calorie_count:
                largest_calorie_count = calorie_counter
            calorie_counter = 0
        else:
            calorie_counter += int(num_string)
    
    return largest_calorie_count

def part_2(data=day1_practice):
    calorie_counter = 0
    largest_calorie_count = [0, 0, 0]
    for num_string in data.split("\n"):
        if num_string == "":
            if calorie_counter > (min_current := min(largest_calorie_count)):
                largest_calorie_count.remove(min_current)
                largest_calorie_count.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(num_string)
    
    return sum(largest_calorie_count)

if __name__ == "__main__":
    print(part_1(day1_data))
    print(part_2(day1_data))