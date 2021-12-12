import re

with open("input.txt", "r") as file:
    numbers = list(map(int, file.readline().split(",")))
    boards = []
    line = file.readline() # throw away
    while line:
        board = []
        for i in range(5):
            line = file.readline()
            board.append(list(map(int, re.split("\\s+", line.strip()))))
        boards.append(board)
        line = file.readline()

    board_masks = [([([False for j in range(5)]) for i in range(5)]) for b in range(len(boards))]

    bingo_board = 0
    numbers_until_bingo = 0

    for k in range(len(boards)):
        board = boards[k]
        matches = 0
        for l in range(len(numbers)):
            number = numbers[l]
            for i in range(5):
                row = board[i]
                for j in range(5):
                    if row[j] == number:
                        matches += 1
                        board_masks[k][i][j] = True

            if matches >= 5: # can't get a bingo with 4 numbers or less.
                current_board_bingo = False
                # check rows
                for i in range(5):
                    row = board_masks[k][i]
                    if sum(row) == 5:
                        current_board_bingo = True

                # check columns
                if not current_board_bingo:
                    for i in range(5):
                        mask = board_masks[k]
                        if sum([mask[0][i], mask[1][i], mask[2][i], mask[3][i], mask[4][i]]) == 5:
                            current_board_bingo = True

                if current_board_bingo:
                    if l > numbers_until_bingo:
                        numbers_until_bingo = l
                        bingo_board = k
                    break

    last_number_called = numbers[numbers_until_bingo]
    sum_of_umasked_numbers = 0

    for i in range(5):
        for j in range(5):
            if not board_masks[bingo_board][i][j]:
                sum_of_umasked_numbers += boards[bingo_board][i][j]
    
    print(sum_of_umasked_numbers * last_number_called)