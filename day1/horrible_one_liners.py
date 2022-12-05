from data import day1_practice, day1_data


def nasty_one_liner(dataset=day1_practice):
    return max([sum([int(item) for item in elf_holdings.split("\n")]) for elf_holdings in dataset.split("\n\n")])

def even_nastier_one_liner(dataset=day1_practice):
    return sum(sorted([sum([int(item) for item in elf_holdings.split("\n")]) for elf_holdings in dataset.split("\n\n")])[-3:])

if __name__ == "__main__":
    print(nasty_one_liner(day1_data))
    print(even_nastier_one_liner(day1_data))