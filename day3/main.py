from data import practice, data as full_data
import string

def part_1(input_data=practice):
    priority_sum = 0
    for rucksack_contents in input_data.split("\n"):
        
        compartment_size = len(rucksack_contents)//2
        first_compartment, second_compartment = set(rucksack_contents[:compartment_size]), set(rucksack_contents[compartment_size:])
        
        match = list(first_compartment & second_compartment)
        
        priority_sum += string.ascii_letters.index(match[0]) + 1
    
    return priority_sum
        
def part_2(input_data=practice):
    priority_sum = 0
    dataset = input_data.split("\n")
    dataset_size = len(dataset)
    for i in range(0, dataset_size, 3):
        elf_1 = set(dataset[i])
        elf_2 = set(dataset[i+1])
        elf_3 = set(dataset[i+2])
        
        match = list(elf_1 & elf_2 & elf_3)
        assert(len(match)==1)
        priority_sum += string.ascii_letters.index(match[0]) + 1
    
    return priority_sum



if __name__ == "__main__":
    assert(part_1()==157)
    print(f"part_1:{part_1(full_data)}")
    assert(part_2()==70)
    print(f"part_2:{part_2(full_data)}")