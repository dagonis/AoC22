if __name__ == '__main__':
    all_pairs = open('input.txt', encoding="utf-8").read().splitlines()
    overlaps_1, overlaps_2 = 0, 0
    for pair in all_pairs:
        left_start, left_end = [int(_) for _ in pair.split(",")[0].split("-")]
        right_start, right_end = [int(_) for _ in pair.split(",")[-1].split("-")]
        # Part 1
        if (left_start <= right_start and left_end >= right_end) or (right_start <= left_start and right_end >= left_end):
            overlaps_1 += 1
        # Part 2
        if (right_start <= left_start <= right_end) or (left_start <= right_start <= left_end):
            overlaps_2 += 1
    print(f"Part 1:{overlaps_1}/Part 2:{overlaps_2}")