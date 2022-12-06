if __name__ == '__main__':
    data = list(enumerate(open('input.txt', encoding="utf-8").read().strip()))
    # part 1
    for i, c in data:
        check = set("".join([_[1] for _ in data[i:i+4]]))
        if len(check) == 4:
            print(f"Start of packet found at position {i+4}")
            break
    # part 2
    for i, c in data:
        check = set("".join([_[1] for _ in data[i:i+14]]))
        if len(check) == 14:
            print(f"Start of packet found at position {i+14}")
            break