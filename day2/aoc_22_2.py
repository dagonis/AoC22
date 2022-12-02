if __name__ == '__main__':
    data = open('input.txt').read().splitlines()
    values = {"A": 1, "B": 2, "C": 3}
    total_score = 0
    # Part 1
    for rps_round in data:
        left, right = rps_round.split(' ')
        right = "A" if right == "X" else "B" if right == "Y" else "C"
        if ord(left) - 1 == ord(right) or (ord(left) + 2 == ord(right)):
            pass
        elif ord(left) + 1 == ord(right) or (ord(left) - 2 == ord(right)):
            total_score += 6
        else:
            total_score += 3
        total_score += values[right]
    print(f"Part 1:{total_score}")
    # Part 2
    total_score = 0
    for rps_round in data:
        left, right = rps_round.split(' ')
        if right == "X":
            total_score += values[chr(ord(left) - 1 if not left == "A" else ord(left) + 2)]
        elif right == "Y":
            total_score += values[left]
            total_score += 3
        else:
            total_score += values[chr(ord(left) + 1 if not left == "C" else ord(left) - 2)]
            total_score += 6
    print(f"Part 2:{total_score}")
