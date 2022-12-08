if __name__ == '__main__':
    data = [[int(val) for val in line] for line in open('input.txt', encoding="utf-8").read().splitlines()]
    row_len, col_len = len(data[0]),len(data[0])
    # Part 1
    visible = 0
    for i in range(row_len):
        for j in range(col_len):
            if i in (0, i == row_len - 1) or j in (0, col_len - 1):
                visible += 1
            else:
                current_value = data[i][j]
                left, right, up, down = True, True, True, True
                for n in range(0, j):
                    if data[i][n] >= current_value:
                        left = False
                        break
                if not left: # Only Continue Checking if the Left is clear
                    for n in range(j + 1, row_len):
                        if data[i][n] >= current_value:
                            right = False
                            break
                    if not right: # Only Continue Checking if the Right is clear
                        for n in range(0, i):
                            if data[n][j] >= current_value:
                                up = False
                                break
                        if not up:
                            for n in range(i + 1, col_len):
                                if data[n][j] >= current_value:
                                    down = False
                                    break
                if any([left, right, up, down]):
                    visible += 1
            j += 1 
        i += 1
    print(f"Part 1:{visible}")
    # Part 2
    scores = []
    for i in range(row_len):
        for j in range(col_len):
            current_value = data[i][j]
            # Check Left
            n = j - 1 if j > 0 else -1
            left_score = 0
            while n >= 0:
                if data[i][n] >= current_value:
                    left_score += 1
                    break
                else:
                    n -= 1
                    left_score += 1
            # Check Right
            n = j + 1 if j < row_len else row_len
            right_score = 0
            while n < row_len:
                if data[i][n] >= current_value:
                    right_score += 1
                    break
                else:
                    n += 1
                    right_score += 1
            # Check Up
            n = i - 1 if i > 0 else -1
            up_score = 0
            while n >= 0:
                if data[n][j] >= current_value:
                    up_score += 1
                    break
                else:
                    n -= 1
                    up_score += 1
            # Check Down
            n = i + 1 if i < col_len else col_len
            down_score = 0
            while n < col_len:
                if data[n][j] >= current_value:
                    down_score += 1
                    break
                else:
                    n += 1
                    down_score += 1
            scenic_score = left_score * right_score * up_score * down_score
            scores.append(scenic_score)
            j += 1 
        i += 1
    print(f"Part 2:{max(scores)}")