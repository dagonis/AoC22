from itertools import accumulate
from collections import defaultdict

if __name__ == '__main__':
    data = open('input.txt', encoding="utf-8").read().splitlines()
    directory_size_dict = defaultdict(int)
    directory_stack = []
    sub_dirs = {}
    for line in data:
        if line.startswith("$"):
            if "cd" in line:
                if line.endswith(".."):
                    directory_stack.pop()
                else:
                    current_directory = line.split(" ")[-1]
                    directory_stack.append(current_directory)
                    directory_size_dict[current_directory] = directory_size_dict.get(current_directory, 0)
                    sub_dirs[current_directory] = []
            elif line.endswith("ls"):
                pass
        else:
            if line.startswith("dir"):
                sub_dirs[current_directory].append(line.split(" ")[-1])
            else:
                for directory in accumulate(directory_stack):
                    directory_size_dict[directory] += int(line.split(" ")[0])
    p1 = 0
    for k, v in directory_size_dict.items():
        if v <= 100000:
            p1 += v
    print(f"Part 1: {p1}")
    candidates = []
    for k, v in directory_size_dict.items():
        if v >= directory_size_dict["/"] - 40_000_000:
            candidates.append(v)
    print(f"Part 2: {min(candidates)}")
