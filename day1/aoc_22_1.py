if __name__ == '__main__':
    data = open('input.txt').read().splitlines()
    current_elf = 0
    elf_dict = {}
    for d in data:
        if not d == '':
            elf_dict[current_elf] = elf_dict.get(current_elf, 0) + int(d)
        else:
            current_elf += 1
    # Part 1
    most_calories = 0
    for k, v in elf_dict.items():
        if v > most_calories:
            most_calories = v
    print(most_calories)
    # Part 2
    sorted_calories = dict(sorted(elf_dict.items(), key=lambda item: item[1]))
    print(sum([elf_dict[_] for _ in list(sorted_calories.keys())[-3:]]))

