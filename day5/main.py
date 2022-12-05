from data import practice_init_state, practice_instruction_set, init_state, instruction_set

class CrateStack9000():
    def __init__(self, raw_init_state=practice_init_state):
        init_state = raw_init_state.split("\n")
        data_raw, indexes_raw = init_state[:-1], init_state[-1]
        self.state = {}
        for position, char in enumerate(indexes_raw):
            if char != " ":
                self.state[int(char)] = [row[position] for row in data_raw if row[position] != " "][::-1]

    def move(self, source, target, quantity):
        for _ in range(quantity):
            self.swap(source, target)

    def swap(self, source, target):
        box = self.state[source].pop()
        self.state[target].append(box)

    def __str__(self) -> str:
        output = ""
        for idx, boxes in self.state.items():
            output += f"{idx}: {boxes}\n"
        output += "=================="
        return output

    def get_top_pile(self):
        print("".join([boxes[-1] for boxes in self.state.values()]))

    def run(self, raw_instruction_set=practice_instruction_set):
        instruction_set = []
        for raw_instruction in raw_instruction_set.split("\n"):
            split_instruction = raw_instruction.split(" ")
            quantity = int(split_instruction[1])
            source = int(split_instruction[3])
            target = int(split_instruction[5])
            instruction_set.append([source, target, quantity])

        for [source, target, quantity] in instruction_set:
            self.move(source, target, quantity)


class CrateStack9001(CrateStack9000):
    def move(self, source, target, quantity):
        self.state[source], boxes = self.state[source][:-quantity], self.state[source][-quantity:]
        self.state[target] += boxes


if __name__ == "__main__":
    crate_stack_part_1 = CrateStack9000(init_state)
    crate_stack_part_1.run(instruction_set)
    crate_stack_part_1.get_top_pile()
    
    crate_stack_part_2 = CrateStack9001(init_state)
    crate_stack_part_2.run(instruction_set)
    crate_stack_part_2.get_top_pile()
