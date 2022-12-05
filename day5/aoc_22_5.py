if __name__ == '__main__':
    data = open('input.txt', encoding="utf-8").read().splitlines()
    initial_positions = []
    for line in data:
        if not line == '':
            initial_positions.append(line)
        else:
            break
    instructions = [_ for _ in data if _.startswith('move')]
    position_dict = {}
    string_positions = {v:k for k, v in enumerate(initial_positions[-1]) if not v == ' '}
    # Part 1
    for position in initial_positions[-1].split():
        position_dict[position] = []
    for crates in initial_positions[-2::-1]:
        for stack, str_position in string_positions.items():
            if crates[str_position].isalpha():
                position_dict[stack].append(crates[str_position])
    for instruction in instructions:
        split_instructions = instruction.split()
        number_to_move, src_stack, dst_stack = int(split_instructions[1]), split_instructions[3], split_instructions[5]
        for _ in range(number_to_move):
            position_dict[dst_stack].append(position_dict[src_stack].pop())
    top_crates = ""
    for k, v in position_dict.items():
        top_crates += v[-1]
    print(f"Part 1:{top_crates}")
    # Part 2
    for position in initial_positions[-1].split():
        position_dict[position] = []
    for crates in initial_positions[-2::-1]:
        for stack, str_position in string_positions.items():
            if crates[str_position].isalpha():
                position_dict[stack].append(crates[str_position])
    for instruction in instructions:
        split_instructions = instruction.split()
        number_to_move, src_stack, dst_stack = int(split_instructions[1]), split_instructions[3], split_instructions[5]
        stack_to_move = []
        for _ in range(number_to_move):
            stack_to_move.append(position_dict[src_stack].pop())
        for crate in stack_to_move[::-1]:
            position_dict[dst_stack].append(crate)
    top_crates = ""
    for k, v in position_dict.items():
        top_crates += v[-1]
    print(f"Part 2:{top_crates}")