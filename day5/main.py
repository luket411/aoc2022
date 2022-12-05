from data import practice_init_state, practice_instruction_set, init_state, instruction_set

class CrateStack9000():
    def __init__(self, raw_init_state=practice_init_state):
        """
        Takes init_state stirng like those in day5/data.py

        Creates dictionary where the name of the stack maps to the list of boxes currently in that stack. The last item of the stack represents the "top" of the box stack
        (yes it easily could be an array, I just wanted to be able to use the index's in the data directly and not have to worry about index 0)

        {
            1: ['A','B','C'],
            2: ['D','E'],
            3: ['F'],
            4: [],
            5: ['G', 'H']
            ...
        }
        """
        init_state = raw_init_state.split("\n")
        data_raw, indexes_raw = init_state[:-1], init_state[-1]
        self.state = {}
        for position, char in enumerate(indexes_raw):
            if char != " ":
                self.state[int(char)] = [row[position] for row in data_raw if row[position] != " "][::-1]

    def move(self, source, target, quantity):
        for _ in range(quantity):
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
        for raw_instruction in raw_instruction_set.split("\n"):
            split_instruction = raw_instruction.split(" ")
            quantity = int(split_instruction[1])
            source = int(split_instruction[3])
            target = int(split_instruction[5])
            self.move(source, target, quantity)


class CrateStack9001(CrateStack9000):
    def move(self, source, target, quantity):
        self.state[source], boxes = self.state[source][:-quantity], self.state[source][-quantity:]
        self.state[target] += boxes


if __name__ == "__main__":
    crate_stack_part_1_practice = CrateStack9000()
    crate_stack_part_1_practice.run()
    crate_stack_part_1_practice.get_top_pile()

    crate_stack_part_1 = CrateStack9000(init_state)
    crate_stack_part_1.run(instruction_set)
    crate_stack_part_1.get_top_pile()

    crate_stack_part_2_practice = CrateStack9001()
    crate_stack_part_2_practice.run()
    crate_stack_part_2_practice.get_top_pile()
    
    crate_stack_part_2 = CrateStack9001(init_state)
    crate_stack_part_2.run(instruction_set)
    crate_stack_part_2.get_top_pile()
