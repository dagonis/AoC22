from string import ascii_letters

if __name__ == '__main__':
    data = open('input.txt').read().splitlines()
    values = {v:k for k, v in enumerate("!" + ascii_letters)}
    # Part 1
    priority = 0
    for sack in data:
        pack_size = int(len(sack)/2)
        front, back = set(sack[0:pack_size]), set(sack[pack_size:])
        priority += values[list(front.intersection(back))[0]]
    print(f"part 1:{priority}")
    # Part 2
    priority = 0
    i = 0
    while i < len(data):
        sacks = data[i:i+3]
        priority += values[list((set.intersection(set(sacks[0]), set(sacks[1]), set(sacks[2]))))[0]]
        i += 3
    print(f"part 2:{priority}")