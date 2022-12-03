from string import ascii_letters

if __name__ == '__main__':
    all_sacks = open('input.txt').read().splitlines()
    priorities = {v:k for k, v in enumerate("_" + ascii_letters)}
    # First Part
    p = 0
    for sack in all_sacks:
        p += priorities[set.intersection(set(sack[0:len(sack)//2]), set(sack[len(sack)//2:])).pop()]
    print(f"1:{p}")
    # Second Part
    i, p = 0, 0
    while i < len(all_sacks):
        sacks = all_sacks[i:i+3]
        p += priorities[set.intersection(set(sacks[0]), set(sacks[1]), set(sacks[2])).pop()]
        i += 3
    print(f"2:{p}")
