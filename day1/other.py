from data import day1_practise, day1_data

def part_1_slower(data=day1_practise):
    calorie_counter = 0
    elf_calorie_counters = []
    for num_string in data.split("\n"):
        if num_string == "":
            elf_calorie_counters.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(num_string)
    
    return sum(sorted(elf_calorie_counters)[-3:])


def part_2_slower(data=day1_practise):
    calorie_counter = 0
    elf_calorie_counters = []
    for num_string in data.split("\n"):
        if num_string == "":
            elf_calorie_counters.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(num_string)
    
    return max(elf_calorie_counters)